import rospy
from mavros_msgs.srv import SetMode
from mavros_msgs.msg import OverrideRCIn
from utils.rover_utils import Rc


class MavrosRover:

    def __init__(self):
        rospy.init_node('mavros_rover')
        self.pup_rc = rospy.Publisher('mavros/rc/override', OverrideRCIn, queue_size=10)
        self.rc_msg = OverrideRCIn()
        self.rc_throttle = Rc(rc_min=1020, rc_max=2006)
        self.rc_steering = Rc(rc_min=1020, rc_max=2006)

    def set_throttle(self, value):
        self.rc_throttle.set_value(value)

    def set_steering(self, value):
        self.rc_steering.set_value(value)

    def set_mode(self, mode):
        rospy.wait_for_service('/mavros/set_mode')
        try:
            set_mode = rospy.ServiceProxy('/mavros/set_mode', SetMode)
            print set_mode(custom_mode=mode)
        except rospy.ServiceException, e:
            print "Failed SetMode: %s" % e

    def send_cmd(self):
        self.rc_msg.channels[2] = self.rc_throttle.rc_value
        self.rc_msg.channels[3] = self.rc_steering.rc_value
        self.pup_rc.publish(self.rc_msg)

    def release_rc(self):
        for i in range(len(self.rc_msg.channels)):
            self.rc_msg.channels[i] = 0
        self.pup_rc.publish(self.rc_msg)
