from dronekit import connect
from dronekit import VehicleMode
from pymavlink import mavutil
import time

# print('connecting to rover')
vehicle = connect('192.168.1.88:14550', wait_ready=True)
print('succeeded')
print "Is Armable?: %s" % vehicle.is_armable
print "System status: %s" % vehicle.system_status.state
print "Mode: %s" % vehicle.mode.name    # settable
print "Armed: %s" % vehicle.armed    # settabl

vehicle.send_mavlink()
vehicle.flush()

master.mav.rc_channels_override_send(1, 1, 0, 0, 0, 0, 0, 0, 0, 0)

vehicle.send_mavlink()


# autopilot.set_mode_auto()

# print('target_system:       {}'.format(autopilot.target_system))
# print('target_component:    {}'.format(autopilot.target_component))
# print('message id:          {}'.format(mavlink.MAVLINK_MSG_ID_MANUAL_CONTROL))
#


# def rc_channels_override_send(self, target_system, target_component, chan1_raw, chan2_raw, chan3_raw, chan4_raw,
#                               chan5_raw, chan6_raw, chan7_raw, chan8_raw, force_mavlink1=False):

#


# msg = None
#
# # wait for autopilot connection
# while msg is None:
#         msg = autopilot.recv_msg()
#
# print msg
#
# autopilot.mav.manual_control()