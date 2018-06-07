#mono vo
roslaunch viso2_ros demo_mono.launch

rostopic echo -p /mytopic > (outputfile).txt

rosbag play (bag file) -r 0.3 
#If your laptopmis not good enough, it won't be in realtime


#mono vo
roslaunch viso2_ros demo.launch

rostopic echo -p /stereo_odometer/pose > (outputfile).txt

rosbag play -r 0.3 --clock (bag file) /kitti/camera_color_left/image_raw:=/stereo_forward/left/image_raw /kitti/camera_color_left/camera_info:=/stereo_forward/left/camera_info /kitti/camera_color_right/image_raw:=/stereo_forward/right/image_raw /kitti/camera_color_right/camera_info:=/stereo_forward/right/camera_info