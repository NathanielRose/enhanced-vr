#!/usr/bin/env python

from __future__ import print_function

import random
import rospy

import moveit_msgs.msg
from moveit_msgs.msg import Constraints, JointConstraint, PositionConstraint, OrientationConstraint, BoundingVolume
from sensor_msgs.msg import JointState
from moveit_msgs.msg import RobotState
import geometry_msgs.msg
from geometry_msgs.msg import Quaternion, Pose
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

from robotics_demo.srv import PositionService, PositionServiceResponse


def new_position(req):
    print("Request: \n{}".format(req.input))
    req.input.pos_x = random.uniform(-1.0, 1.0)
    req.input.pos_z = random.uniform(-1.0, 1.0)

    return PositionServiceResponse(req.input)


def translate_position_server():
    rospy.init_node('position_server')
    s = rospy.Service('position_service', PositionService, new_position)
    print("Ready to move Robot!")
    rospy.spin()


if __name__ == "__main__":
    translate_position_server()
