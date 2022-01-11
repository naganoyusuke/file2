#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

rospy.init_node('fourth')
pub = rospy.Publisher('fourth_up',Int32, queue_size=1)
rate = rospy.Rate(20)
n = 0
def cb(message):
	pub.publish(message.data*4)

if __name__== '__main__':
	rospy.init_node('fourth')
	sub = rospy.Subscriber('third_up', Int32, cb)
	rospy.spin()
