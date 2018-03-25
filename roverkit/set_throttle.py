from pymavlink import mavutil
from dronekit import connect
from dronekit import VehicleMode
import time

# https://research.ece.ncsu.edu/wireless/MadeInWALAN/CentMeshWikiBackup/tracwiki/raw-attachment/wiki/HardWare/MobileNode/Programming/Tutorial_drone-with-mavutilusage.pdf

print('connecting to rover')
conn = mavutil.mavlink_connection(device='192.168.1.88:14550', baud=921600)
data_from_mavproxy = conn.recv_match(type='HEARTBEAT', blocking=True)
print(data_from_mavproxy)
conn.set_mode_manual()
conn.motors_armed_wait()
time.sleep(1.0)

values = [0] * 8
values[2] = 1000
values[3] = 1000

conn.mav.rc_channels_override_send(conn.target_system, conn.target_component, *values)


#
# # master.mav.request_data_stream_send(master.target_system, master.target_component, mavutil.mavlink.MAV_DATA_STREAM_ALL, 4, 1)
#
# print("Heartbeat from APM (system %u component %u)" % (master.target_system, master.target_system))
# # master.set_mode_manual()
# # master.motors_armed()
#
