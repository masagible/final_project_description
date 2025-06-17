#!/usr/bin/env python3


import rospy
from sensor_msgs.msg import Image # message type
from cv_bridge import CvBridge # convert between ROS and OpenCV images
import cv2 # OpenCV library


def callback(data):
   # create a CvBridgeobject
   br = CvBridge()
   rospy.loginfo("receiving video frame")
   # Convert ROS Image message to OpenCV image
   current_frame = br.imgmsg_to_cv2(data)
   # Display image
   cv2.imshow("camera", current_frame)
   cv2.waitKey(1)


def receive_message():
   rospy.init_node('cv_sub', anonymous=True)
   rospy.Subscriber('/camera/image', Image, callback)
   rospy.spin()
   # Close down the video stream when done
   cv2.destroyAllWindows()


if __name__ == '__main__':
   receive_message()