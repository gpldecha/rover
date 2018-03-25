import threading
from rover_mavros import MavrosRover
from joystick import Joystick
import copy


def is_close(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


class Control(threading.Thread):

    def __init__(self, joystick, rover):
        threading.Thread.__init__(self)

        self.joystick = joystick
        self.rover = rover

        self.rover.rc_throttle.v_min = -1.0
        self.rover.rc_throttle.v_max = 1.0

        self.cmd_throttle_value = 0.0
        self.cmd_steering_value = 0.0

        self.stop_event = threading.Event()

    def connect_callback(self):
        self.rover.connect('udpin:192.168.1.88:14550')

    def run(self):
        print('run')
        while not self.stop_event.is_set():
            x = copy.copy(self.joystick.axis_states['x'])
            y = copy.copy(self.joystick.axis_states['y'])

            self.rover.set_throttle(-y)
            self.rover.set_steering(-x)

            self.rover.send_cmd()
            self.stop_event.wait(0.002)

        self.rover.release_rc()
        print('stopped')

    def stop(self):
        if self.isAlive():
            self.stop_event.set()

if __name__ == '__main__':
    rover = MavrosRover()

    joystick = Joystick()
    joystick.start()

    control = Control(joystick, rover)
    control.start()

    control.stop()
    joystick.stop()