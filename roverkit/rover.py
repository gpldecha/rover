import time
from pymavlink import mavutil
from utils.rover_utils import linear_scaling
from dronekit import connect
from dronekit import VehicleMode
# https://gist.github.com/vo/9362500
from utils.rover_utils import Rc


class Rover:

    def __init__(self):
         self.master = None
         self.is_connected = False
         self.rc_throttle = Rc(rc_min=1020, rc_max=2006)
         self.rc_steering = Rc(rc_min=984, rc_max=2006)
         mavutil.set_dialect("ardupilotmega")

    def connect(self, device):
        self.master = mavutil.mavlink_connection(device=device, baud=921600)

        print("Waiting for APM heartbeat")
        self.master.wait_heartbeat()
        # self.master.mav.request_data_stream_send(self.master.target_system, self.master.target_component, mavutil.mavlink.MAV_DATA_STREAM_ALL, 4, 1)

        print("Heartbeat from APM (system %u component %u)" % (self.master.target_system, self.master.target_system))
        self.master.set_mode_manual()
        self.master.motors_armed()
        print('target_system    {}'.format(self.master.target_system))
        print('target_component {}'.format(self.master.target_component))
        self.is_connected = True

    def send_cmd(self):
        if not self.is_connected: return
        thrott = self.rc_throttle.rc_value
        steer = self.rc_steering.rc_value
        print('self.rc_throttle.rc_value: {}'.format(thrott))
        self.master.mav.rc_channels_override_send(self.master.target_system, self.master.target_component, 0, 0, thrott, steer, 0, 0, 0, 0)

    def release_rc(self):
        if self.master is None: return
        self.master.mav.rc_channels_override_send(self.master.target_system, self.master.target_component, 0, 0, 0, 0, 0, 0, 0, 0)
