#!/bin/bash

shell=`basename $SHELL`
echo "Activating ROS..."
source /opt/ros/kinetic/setup.$shell

echo "Setup ROS_HOSTNAME..."
export HOSTNAME=$HOSTNAME
export ROS_HOSTNAME=$HOSTNAME.local

echo "Activating development environment..."
source catkin_ws/devel/setup.$shell