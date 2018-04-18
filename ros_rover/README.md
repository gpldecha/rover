## IMU filter

The objective is to get position estimate from linear acceleration. This is difficult as it requires a double integration
of a noisy singal.

## Camera

* ```roslaunch raspicam_node camera.launch```
  -  /raspicam/image/compressed: sensor_msgs/CompressedImage
* ``` rosrun image_transport republish compressed in:=/raspicam/image raw out:=/raspicam/image_raw```
* ``` ROS_NAMESPACE=raspicam rosrun image_proc image_proc```
* ``` rosrun viso2_ros mono_odometer image:=/raspicam/image_rect```

[raspicam_node](https://github.com/UbiquityRobotics/raspicam_node)

### calibration

[OpenCV camera model](https://docs.opencv.org/2.4/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html)

[What Is Camera Calibration?](https://uk.mathworks.com/help/vision/ug/camera-calibration.html)

## SLAM

[ORB-SLAM2](https://github.com/raulmur/ORB_SLAM2)

[ROS ORB-SLAM2](https://github.com/ildoonet/ros-orb-slam2)
  * might have to train new visual vocabulary 

[LSD-SLAM](https://github.com/kevin-george/lsd_slam/wiki/LSD-SLAM-with-ROS-and-Ubuntu-16.04)
  * can get somewhate working (orientation can be extracted)
  
 [VIORB](https://github.com/jingpang/LearnVIORB) combining IMU with SLAM seems like a good approach.
 
 [DSO ROS](https://github.com/JakobEngel/dso_ros)

**References**
* [qml-imu](https://github.com/chili-epfl/qml-imu) 
* [robot_pose_ekf](http://wiki.ros.org/robot_pose_ekf)

https://people.eecs.berkeley.edu/~chaene/cvpr17tut/SLAM.pdf
