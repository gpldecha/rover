import signal
import threading
from rover_mavros import MavrosRover
from joystick import Joystick
import copy
import time


def signal_handler(_, __, stop_callback):
    print('stop event set')
    stop_callback()

stopper = threading.Event()


class Control:

    def __init__(self, joystick, rover):

        self.joystick = joystick
        self.rover = rover

        self.rover.rc_throttle.v_min = -1.0
        self.rover.rc_throttle.v_max = 1.0

        self.cmd_throttle_value = 0.0
        self.cmd_steering_value = 0.0

        self.stop_flag = False

    def run(self):
        print('run')
        while not self.stop_flag:
            x = copy.copy(self.joystick.axis_states['x'])
            y = copy.copy(self.joystick.axis_states['y'])

            self.rover.set_throttle(-y)
            self.rover.set_steering(-x)

            self.rover.send_cmd()
            time.sleep(0.002)

        self.rover.release_rc()
        print('stopped')

    def stop(self):
        self.stop_flag = True

if __name__ == '__main__':

    rover = MavrosRover()

    joystick = Joystick()
    joystick.start()

    control = Control(joystick, rover)

    g = lambda singal, frame: signal_handler(signal, frame, control.stop)
    signal.signal(signal.SIGINT, g)

    control.run()
    joystick.stop()

