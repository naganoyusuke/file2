#!/usr/bin/env python3

# "SPDX-License-Identifier:BSD-2
# *Copyright(c)2022 Ryuich Ueda. All rights reserved.
# *Copyright(c)2022 Yusuke Nagano.All rights reserved.

import rospy
from std_msgs.msg import Int32

rospy.init_node('count')
pub =rospy.Publisher('count_up', Int32, queue_size=1)
rate = rospy.Rate(20)
n = 0
while not rospy.is_shutdown():
	n += 1
	pub.publish(n)
	rate.sleep()
