# AGV-OTA (ROS2 Jazzy)
This repository includes the AGV ROS2 Jazzy packages of AGV-OTA.

![Image of AGV](https://github.com/inomuh/agv/blob/main/images/agv_gazebo.png)

- agv_description: It is the sub-package containing urdf and mesh files of the AGV.
- agv_simulation: It is a sub-package containing the package and launch files required for the simulation of the AGV.
- agv_slam: It is a sub-package containing the slam_toolbox launch files.
- agv_navigation: It is a sub-package containing the navigation launch and config files.

Video demonstration:
https://youtu.be/4bqdRWkYXvI

### For other AGV ROS Packages:
https://github.com/inomuh/agvpc_ros

https://github.com/inomuh/agvsim_v1_ros

https://github.com/inomuh/agvpc_ros2

https://github.com/inomuh/agvsim_v2_ros

Launch Command:
---------------
### Warning !!!
Before using launch commands, you must unzip ~/agv/agv_description/meshes/OTAv07_meshes/OTA-v0.7.tar.xz file..
-------------------------------------------------------------------------------------------------------------
Gazebo Launching:

    $ ros2 launch agv_simulation agv_spawn.launch.py
    
SLAM Mapping Launching:

    $ ros2 launch agv_slam agv_slam.launch.py
    
Navigation Launching:

    $ ros2 launch agv_navigation agv_navigation.launch.py


<img width="1766" height="1121" alt="image" src="https://github.com/user-attachments/assets/94f21047-0e8e-4e0c-bc69-43ddf163ea85" />
    
-----------------------------------------------------------------------------------------------------------------------
Requirements:
-------------
- In order for the "joint_state_publisher" to work, "joint_state_publisher_gui" package must be downloaded to your computer.

        $ sudo apt update && sudo apt install ros-$ROS_DISTRO-joint-state-publisher-gui
        
- In order for the "joint_state_controller" to work, "joint_state_controller_gui" package must be downloaded to your computer.

        $ sudo apt install ros-$ROS_DISTRO-ros-controllers
        
- In order for the SLAM to work, "slam_toolbox" package must be downloaded to your workspace.
        
        $ cd ~/catkin_ws/src && git clone https://github.com/SteveMacenski/slam_toolbox.git -b ros2
        
- In order for the sensors to work properly, "gazebo_ros_pkgs" files must be downloaded to your computer.

        $ sudo apt-get install ros-$ROS_DISTRO-gazebo-ros-pkgs
        
- In order for the navigation tools to work properly, "ros-navigation" files must be downloaded to your computer.

        $ sudo apt-get install ros-$ROS_DISTRO-ros-navigation
        
-------------------------------------------------------------------------------
