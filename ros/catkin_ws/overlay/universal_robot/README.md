# Overlay for `universal_robot` (February-April 2021)

These files were added, uncommitted, inside the `ros-industrial/universal_robot` clone of the
original catkin workspace (`src/universal_robot/`). They are the first UR10 bridge to Unity
and were superseded by the standalone `ros/catkin_ws/src/ur10_moveit` package in April 2021,
but are kept because they were never committed anywhere else.

To reproduce the original layout, copy them over the `universal_robot` submodule:

    cp -r ros/catkin_ws/overlay/universal_robot/. ros/catkin_ws/src/universal_robot/

- `ur10_moveit_config/launch/pickandplaceUR10.launch` starts the TCP endpoint, the mover
  service and the MoveIt demo for the UR10.
- `ur10_moveit_config/scripts/`, `msg/`, `srv/` are the earlier versions of the
  `ur10_moveit` scripts and interfaces.
- `ur_description/urdf/ur10.urdf` is the expanded UR10 URDF used for the Unity import.
