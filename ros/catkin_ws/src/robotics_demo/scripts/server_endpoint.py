#!/usr/bin/env python
import sys
import rospy
import tf
import copy

from ros_tcp_endpoint import TcpServer, RosPublisher, RosSubscriber, RosService
from robotics_demo.msg import PosRot, UnityColor
from robotics_demo.srv import PositionService

#import moveit_commander
import random


#from geometry_msgs.msg import Pose, Point, Quaternion

#from ur10_moveit_config.srv import UR10MoverService, MoverServiceRequest, MoverServiceResponse

joint_names = ['joint_00', 'joint_01', 'joint_02', 'joint_03', 'joint_04', 'joint_05', 'joint_06']


def main():
    ros_node_name = rospy.get_param("/TCP_NODE_NAME", 'TCPServer')
    buffer_size = rospy.get_param("/TCP_BUFFER_SIZE", 1024)
    connections = rospy.get_param("/TCP_CONNECTIONS", 10)
    tcp_server = TcpServer(ros_node_name, buffer_size, connections)
    rospy.init_node(ros_node_name, anonymous=True)

    # Setup UR10 Robot to standart position 
    # group = moveit_commander.MoveGroupCommander("manipulator") # UR10 Moveit Group
    # joint_goal = goal.get_current_values()

    
    tcp_server.start({
        'pos_srv': RosService('position_service', PositionService),
        'pos_rot': RosPublisher('pos_rot', PosRot, queue_size=10),
        'color': RosSubscriber('color', UnityColor, tcp_server)
    })
    
    rospy.spin()


if __name__ == "__main__":
    main()
