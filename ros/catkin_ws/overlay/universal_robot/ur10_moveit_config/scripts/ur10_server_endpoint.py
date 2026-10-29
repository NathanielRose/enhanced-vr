#!/usr/bin/python python

import rospy

from ros_tcp_endpoint import TcpServer, RosPublisher, RosSubscriber, RosService
from ur10_moveit_config.msg import UR10MoveitJoints, UR10Trajectory
from ur10_moveit_config.srv import UR10MoverService


def main():
    ros_node_name = rospy.get_param("/TCP_NODE_NAME", 'TCPServer')
    tcp_server = TcpServer(ros_node_name)
    rospy.init_node(ros_node_name, anonymous=True)

    # Start the Server Endpoint with a ROS communication objects dictionary for routing messages
    tcp_server.start({
        'SourceDestination_input': RosPublisher('SourceDestination', UR10MoveitJoints, queue_size=10),
        'UR10Trajectory': RosSubscriber('UR10Trajectory', UR10Trajectory, tcp_server),
        'ur10_moveit': RosService('ur10_moveit', UR10MoverService)
    })
    
    rospy.spin()


if __name__ == "__main__":
    main()
