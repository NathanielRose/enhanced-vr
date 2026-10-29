# Third-party code and dependencies

Everything the project built on, with the exact revision that was checked out in the
original workspace. Submodules are pinned in `.gitmodules`; the rest are documented here
and not vendored.

## Submodules

| Path | Repository | Pinned revision | Licence | Role |
|---|---|---|---|---|
| `ros/catkin_ws/src/universal_robot` | https://github.com/ros-industrial/universal_robot (`kinetic-devel`) | `06d8b9e` (1.2.7, Nov 2019) | BSD-3 | UR10 description, kinematics and MoveIt configs that `ur10_moveit` was generated from |
| `ros/catkin_ws/src/ROS-TCP-Endpoint` | https://github.com/Unity-Technologies/ROS-TCP-Endpoint (`dev`) | `49d7b71` (Jan 2021) | Apache-2.0 | ROS node that serialises messages to and from Unity |
| `ros/catkin_ws/src/moveit_msgs` | https://github.com/ros-planning/moveit_msgs | `3175099` (0.11.1) | BSD-3 | MoveIt message definitions used by the mover services |
| `unity/pick_and_place/ROS/src/ros_tcp_endpoint` | https://github.com/Unity-Technologies/ROS-TCP-Endpoint | `8a1dde6` (Dec 2020) | Apache-2.0 | Same bridge, the version the Docker image was built with |
| `unity/pick_and_place/ROS/src/moveit_msgs` | https://github.com/ros-planning/moveit_msgs | `3175099` (0.11.1) | BSD-3 | |
| `unity/pick_and_place/ROS/src/niryo_one_ros` | https://github.com/NiryoRobotics/niryo_one_ros | `d1aaea7` (2.3.1) | GPL-3.0 | Niryo One stack from the original Unity tutorial; only needed to rebuild the Niryo demo |

Initialise them with `git submodule update --init --recursive`.

## Vendored copies

| Path | Origin | Revision | Licence |
|---|---|---|---|
| `unity/pick_and_place/ROS/src/ur_msgs` | https://github.com/ros-industrial/ur_msgs | 1.2.1 (copied into the workspace in 2021) | BSD-3 |
| `unity/pick_and_place/ROS/src/niryo_one_urdf` | Unity Robotics Hub tutorial | as imported | Apache-2.0 / GPL-3.0 (Niryo meshes) |
| `unity/pick_and_place/PickAndPlaceProject/Assets/URDF/UR10` and `unity/ur10_robotiq_gripper/ur3_with_gripper/ur_description` | `ur_description` from ros-industrial/universal_robot | 1.2.7 | BSD-3 |
| `unity/ur10_robotiq_gripper/ur3_with_gripper/robotiq_2f_140_gripper_visualization` | https://github.com/ros-industrial/robotiq | 2021 checkout | BSD-2 |
| `ros/catkin_ws/src/ur10_moveit/ur_description`, `ros/catkin_ws/src/ur3_moveit/URDF` | same `ur_description` meshes | 1.2.7 | BSD-3 |

## Base of `unity/pick_and_place`

`unity/pick_and_place` is the `tutorials/pick_and_place` tutorial of
https://github.com/Unity-Technologies/Unity-Robotics-Hub (Apache-2.0), forked in December
2020 and modified for the UR10. Its `LICENSE`, `Third Party Notices.md` and the original
landing-page README (`UNITY_ROBOTICS_HUB_README.md`) are kept in that folder. The Unity
project pulls these packages through `Packages/manifest.json`:

| Package | Version |
|---|---|
| `com.unity.robotics.urdf-importer` | https://github.com/Unity-Technologies/URDF-Importer `v0.1.2` (thesis text: v0.5.5) |
| `com.unity.robotics.ros-tcp-connector` | https://github.com/Unity-Technologies/ROS-TCP-Connector `v0.1.2` (thesis text: v0.5.0) |

## Used during the project but not included

| What | Revision / version | Notes |
|---|---|---|
| https://github.com/fmauch/universal_robot (`kinetic-devel`) | `c5a65a5` | Felix Exner's fork, used by the Docker-based workspace in early 2021 and the original gitlink of the catkin workspace |
| https://github.com/Unity-Technologies/Unity-Robotics-Hub | `67b0620` (v0.1.2, Jan 2021), `1d16f11` (`dev`, Jan 2021), `cb26e33` (Mar 2021) | Upstream revisions that were cloned alongside the fork while tracking the tutorial |
| https://github.com/Unity-Technologies/Robotics-Object-Pose-Estimation | `d8fb37e` (Mar 2021) | Evaluated for the gripper pose-estimation idea listed under future work |
| https://github.com/gtatiya/Hacking-SotA-UR5 | `f717942` | Reference for UR + Robotiq gripper control |
| https://github.com/Danfoa/robotiq_2finger_grippers | `42b0a40` | Robotiq 2-finger gripper ROS driver, reference only |
| https://github.com/StanleyInnovation/robotiq_85_gripper | `4c705d4` | Robotiq 85 gripper ROS packages, reference only (the URL no longer resolves) |
| Brain & Behaviour Lab `enhance-gripper` workspace (private Imperial GitLab, `bbl/enhance-gripper`) | `ccef2b9` | The lab's physical UR10 + Robotiq + MoveIt workspace that the simulation mirrors; its `.rosinstall` pulls `moveit`, `moveit_msgs`, `moveit_resources`, `moveit_tutorials`, `moveit_visual_tools`, `geometric_shapes`, `panda_moveit_config` and `rviz_visual_tools` |
| SteamVR Unity Plugin 2.7.3 | | HTC Vive input in the experiment build |
| SensoMotoric Instruments (SMI) Eye Tracking HMD Unity SDK | 2016 | Proprietary; drove the gaze input and 5-point calibration |
| Gaze_Block_Building (Sophiya Chiang, Imperial MSc 2019) | | Prior lab Unity project with the SMI SDK, used as reference for the gaze integration |
| Unity 2020.3.11f1, ROS Melodic, MoveIt, catkin tools 0.6.1, Docker, PhysX 4 (Temporal Gauss-Seidel solver) | | Toolchain described in the thesis |
