import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
    nav_pkg = get_package_share_directory('nav2_bringup')
    this_pkg = get_package_share_directory('agv_navigation')
    map_pkg = get_package_share_directory('agv_slam')

    nav_params = os.path.join(this_pkg, 'params', 'nav_params.yaml')
    map_file = os.path.join(map_pkg, 'maps', 'nav_map.yaml')

    robot_localization_node = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_node',
        output='screen',
        parameters=[
            os.path.join(this_pkg, 'params', 'ekf.yaml'),
            {'use_sim_time': True}
        ],
    )

    nav_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(this_pkg, 'launch', 'navigation_launch.py')
        ),
        launch_arguments={
            'params_file': nav_params,
            'use_sim_time': 'true',
        }.items()
    )

    map_server_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav_pkg, 'launch', 'localization_launch.py')
        ),
        launch_arguments={
            'params_file': nav_params,
            'use_sim_time': 'true',
            'map': map_file,
        }.items()
    )

    return LaunchDescription([
        robot_localization_node,
        map_server_launch,  
        nav_launch,         
    ])