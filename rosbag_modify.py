#!/usr/bin/env python
import rosbag

from goal_tracking.msg import GoalStatus
from std_msgs.msg import Time
import rospy

bag = rosbag.Bag('S03_A1_M2_S5_D50_N99_2016-08-17-17-36-38.bag')
output = rosbag.Bag('output.bag', 'w')

# time = rospy.Time(1471475824, 365837284)

goal = GoalStatus()
i = 1;
for topic, msg, t in bag.read_messages(topics=['/goal_status']):
	
	if i != 10768: 
		# print "t: secs ", t.secs
		# print "t: nsecs: ", t.nsecs
		# print "t: ", t
		# print msg.goal_id
		# print msg.goal_stat
		# print "time stamp ", msg.stamp
		output.write(topic, msg)
		# print "I in WHILE" , i
		
		
	if i == 10768: 
		print "MATHCHED"
		# print msg.goal_id
		# print msg.goal_stat
		# print msg.stamp
		# print t
		print "I in IF", i
		goal.stamp = msg.stamp
		goal.goal_id = 3
		goal.goal_stat = True
		output.write('/goal_status', goal)
	
	i = i+1
# 	if t != time: 
# 		output.write(topic, msg)

# 	if t == time: 
# 		print "MATHCHED"
# 		print msg.goal_id
# 		print msg.goal_stat
# 		print msg.stamp
# 		print t

# 		goal.stamp = msg.stamp
# 		goal.goal_id = 3
# 		goal.goal_stat = True
# 		output.write('/goal_status', goal )
# 		print "BYE"

for topic, msg, t in bag.read_messages(topics=['/joy']):
	output.write(topic, msg)

for topic, msg, t in bag.read_messages(topics=['/eef_pose']):
	output.write(topic, msg)

bag.close()
output.close()

# bag = rosbag.Bag('output.bag')

# for topic, msg, t in bag.read_messages(topics=['/goal_status']):
# 	print msg
# 	print t

# bag.close()   