#!/usr/bin/env python
# license removed for brevity
import copy

import numpy as np
import rospy
from sensor_msgs.msg import Imu


class DataBias:

    def __init__(self, data_size, num_samples):
        self.count = 0
        self.bias = np.zeros(data_size)
        self.num_samples = num_samples
        self.has_bias = False

    def update(self, values):
        if self.count < self.num_samples:
            self.bias = self.bias + values
            self.count += 1
        elif self.count == self.num_samples:
            self.bias /= float(self.num_samples)
            self.count += 1
            self.has_bias = True

    def reset(self):
        self.count = 0
        self.bias.fill(0.)
        self.has_bias = False

    def get_bias(self):
        return self.bias


def imu2vec(imu_data, vector):
    vector[0] = imu_data.linear_acceleration.x
    vector[1] = imu_data.linear_acceleration.y
    vector[2] = imu_data.linear_acceleration.z
    vector[3] = imu_data.angular_velocity.x
    vector[4] = imu_data.angular_velocity.y
    vector[5] = imu_data.angular_velocity.z


def subtract_imu_bias(imu_data, bias):
    imu_data.linear_acceleration.x -= bias[0]
    imu_data.linear_acceleration.y -= bias[1]
    imu_data.linear_acceleration.z -= bias[2]

    imu_data.angular_velocity.x -= bias[3]
    imu_data.angular_velocity.y -= bias[4]
    imu_data.angular_velocity.z -= bias[5]


class IMUFilter:

    def __init__(self, topic_name='/mavros/imu/data'):
        rospy.Subscriber(topic_name, Imu, self._callback)
        self.pub = rospy.Publisher('/rover/imu/data', Imu, queue_size=1)
        self.data_bias = DataBias(6, 50)
        self.imu_data_vector = np.zeros(6)
        self.filtered_imu_data = None

    def _callback(self, data):
        imu2vec(data, self.imu_data_vector)
        self.data_bias.update(self.imu_data_vector)
        if self.data_bias.has_bias:
            self.filtered_imu_data = copy.deepcopy(data)
            subtract_imu_bias(self.filtered_imu_data, self.data_bias.get_bias())
            self.pub.publish(self.filtered_imu_data)


if __name__ == '__main__':

    rospy.init_node('imu_filter', anonymous=True)
    imu_filter = IMUFilter()
    rospy.spin()


