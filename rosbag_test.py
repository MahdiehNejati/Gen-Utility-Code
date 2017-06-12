#!/bin/
import rosbag

from goal_tracking.msg import GoalStatus

# bag = rosbag.Bag('testing.bag', 'w')

# try: 
# 	goal = GoalStatus()
# 	goal.goal_id = 5

# 	bag.write('/goal_status', goal.goal_id)

# finally: 
# 	bag.close

bag = rosbag.Bag('test.bag')
for topic, msg, t in bag.read_messages(topics=['goal_status']):
    print msg
bag.close()