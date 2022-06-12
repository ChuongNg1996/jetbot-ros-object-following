# Simple Object-Following Jetbot 
A simple implementation of object following for Jetbot. 

## Project Description
The project aims to contruct a Jetbot that detects an object on its camera frame and follow it. The object of chose in this example is "person".

The project uses: 
* [ROS Framework](http://wiki.ros.org/) (on Ubuntu) to alleviate concurrency management and module communication.
* [Jetbot](https://jetbot.org/master/), which is a differential wheeled robot and its ros package [jetbot_ros](https://github.com/dusty-nv/jetbot_ros) for motor control.
* [jetson-inference](https://github.com/dusty-nv/jetson-inference) which is an optimized AI framework for Jetson board.

## Installation & Implementation
* Install Python.
* [Install ROS](http://wiki.ros.org/melodic/Installation/Ubuntu) (any version).
* At /usr/home/"name" ("name" is arbitrary), create a ROS workspace. On terminal: 
   ```sh
   mkdir -p ~/catkin_ws/src
   ```
* Go to the created ROS workspace, clone the [jetbot_ros](https://github.com/dusty-nv/jetbot_ros) repo (choose the correct path for your ROS) and `jetbot-ros-object-following` package and build them. On terminal: 
   ```sh
   cd ~/catkin_ws/src
   git clone https://github.com/dusty-nv/jetbot_ros -b melodic
   git clone https://github.com/ChuongNg1996/jetbot-ros-object-following
   cd ..
   catkin_make
   ```
* Download and build [jetson-inference](https://github.com/dusty-nv/jetson-inference) from this [GUIDE](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md).
* Run the launch file.
   ```sh
   roslaunch object_detection_1 object_dectection_1.launch
   ```
## Debugging 
* Use `rostopic list` to see available ROS topics.
* Use `rostopic echo /jetbot_motors/cmd_str` to see if the messages are read.
