import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument


def generate_launch_description():
    pkg_four_wheel = get_package_share_directory('four_wheel')
    nav2_bringup_dir = get_package_share_directory('nav2_bringup')

    map_yaml_path = os.path.join(os.path.expanduser('~'), 'ros2_ws', 'maps', 'my_map.yaml')
    nav2_params_path = os.path.join(pkg_four_wheel, 'config', 'nav2_params.yaml')

    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_bringup_dir, 'launch', 'bringup_launch.py')
        ),
        launch_arguments={
            'map': map_yaml_path,
            'params_file': nav2_params_path,
            'use_sim_time': 'true',
	    'use_composition': 'True',
            'container_name': 'nav2_container'
        }.items()
    )

    return LaunchDescription([nav2_launch])
