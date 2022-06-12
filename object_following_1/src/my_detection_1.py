#!/usr/bin/python
#
# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
#

import jetson.inference
import jetson.utils
import rospy
import time
from std_msgs.msg import String


net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.gstCamera(640,480,"/dev/video0")      # '/dev/video0' for V4L2
display = jetson.utils.glDisplay() # 'my_video.mp4' for file

resolution_x = 640
resolution_y = 480
tolerance_x = 70
lower_x = (resolution_x - tolerance_x)/2
upper_x = (resolution_x + tolerance_x)/2

# while display.IsOpen():
# 	img, width, height = camera.CaptureRGBA()
# 	detections = net.Detect(img, width, height)
# 	display.RenderOnce(img, width, height)
# 	display.SetTitle("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

def cv_node():
    pub = rospy.Publisher('/jetbot_motors/cmd_str', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(20) # 10hz
    # while not rospy.is_shutdown() and display.IsOpen():
    while not rospy.is_shutdown():

        while display.IsOpen():
            img,width,height = camera.CaptureRGBA()
            detections = net.Detect(img, width, height)
        
            if len(detections):
                for i in detections:
                    print(i.ClassID)
                    #if i.ClassID == 1 or i.ClassID == 16 or i.ClassID == 86 or i.ClassID == 65 or i.ClassID == 18:
		    if i.ClassID == 1:
                        if i.Center[0] >= lower_x and i.Center[0] <= upper_x:
                            pub.publish ("backward")
                        elif i.Center[0] < lower_x:
                            pub.publish ("right")
                        elif i.Center[0] > upper_x:
                            pub.publish ("left")
                        else:
                            pub.publish ("stop")
                        #time.sleep(0.3)
                        break

                else:
                   pub.publish ("stop")
            else:
                pub.publish ("stop")
    
            #display.RenderOnce(img, width, height)
            #display.SetTitle("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

        
        # hello_str = "hello world %s" % rospy.get_time()
        # rospy.loginfo(hello_str)
        # pub.publish(hello_str)



        rate.sleep()

if __name__ == '__main__':
    try:
        cv_node()
    except rospy.ROSInterruptException:
        pass
