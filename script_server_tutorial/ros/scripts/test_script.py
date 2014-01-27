#!/usr/bin/python

import roslib
roslib.load_manifest('script_server_tutorial')
import rospy

from simple_script_server import *
sss = simple_script_server()

if __name__ == "__main__":
	rospy.init_node("test_script")

	# move arm to a predefine position, uncomment the following line 
	sss.move("arm","folded", False)

	# or uncomment the following line to move the arm to the desired pose
	#sss.move("arm", [[0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0]], False)

	# move torso to a predefine position, uncomment the following line 
	#sss.move("torso","front_extreme", False)

	# move tray to a predefine position, uncomment the following line 
	#sss.move("tray","down", False)

	# move head to a predefine position, uncomment the following line
	#sss.move("head","back", False)

	# move head to a predefine position, uncomment the following line
	#sss.move("sdh","cylopen", False)

	#you can check existing predefine pose by the using the following command in a terminal
	#$rosparam list | grep script_server
