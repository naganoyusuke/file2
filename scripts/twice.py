#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
rospy.init_node('twice')
pub = rospy.Publisher('twice_up',Int32,queue_size=1)
rate = rospy.Rate (10)
n = 0
def cb(message):
	pub.publish(message.data*2)
if __name__ =='__main__':
	rospy.init_node('twice')
	sub = rospy.Subscriber('count_up' , Int32, cb)
	rospy.spin()
