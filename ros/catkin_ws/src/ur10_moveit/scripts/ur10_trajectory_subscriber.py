#!/usr/bin/env python
"""
    Subscribes to SourceDestination topic.
    Uses MoveIt to compute a trajectory from the target to the destination.
    Trajectory is then published to PickAndPlaceTrajectory topic.
"""
import rospy

from ur10_moveit.msg import UR10MoveItJoints, UR10Trajectory
from moveit_msgs.msg import RobotTrajectory


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "\nI heard:\n%s", data)

def listener():
    rospy.init_node('UR10_Trajectory_Subscriber', anonymous=True)
    rospy.Subscriber("SourceDestination", UR10MoveItJoints, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
