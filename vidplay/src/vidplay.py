#! /usr/bin/python
from __future__ import print_function

import time

import roslib
roslib.load_manifest('vidplay')
import sys
import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError

from std_msgs.msg import String
from sensor_msgs.msg import Image

VIDEO_FILE = '/home/nvidia/VidTest/driving.mp4'

def main(args):
  print("Initializing...")
  bridge = CvBridge()
  image_pub = rospy.Publisher("vidplay", Image) # from sensor_msgs.msg import Image
  rospy.init_node('vidplay', anonymous=True)
  print("Playing video...")
  # Play video from file:
  LOOP_COUNT = 1
  for i in range(LOOP_COUNT):
    cap = cv2.VideoCapture(VIDEO_FILE)
    while(True):
      # Capture frame-by-frame
      ret, frame = cap.read()
      if not ret:
        break
      # Try to convert frame to ROS Image message type
      try:
        image_msg = bridge.cv2_to_imgmsg(frame, "bgr8")
        image_pub.publish(image_msg)
      except CvBridgeError as e:
        print(e)
      time.sleep(1.0/60.0)
      

  print("Finished playing video, closing")



if __name__ == '__main__':
    main(sys.argv)
