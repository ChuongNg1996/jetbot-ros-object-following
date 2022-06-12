cmake_minimum_required(VERSION 3.0.2)
project(object_following_1)

find_package(catkin REQUIRED std_msgs darknet_ros_msgs)

catkin_package(CATKIN_DEPENDS std_msgs darknet_ros_msgs)

include_directories(${catkin_INCLUDE_DIRS})

catkin_install_python(PROGRAMS src/my_detection_1.py 
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})



