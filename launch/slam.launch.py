import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    pkg_path = get_package_share_directory('four_wheel')
    slam_params = os.path.join(pkg_path, 'config', 'mapper_params_online_async.yaml')

    slam_toolbox = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('slam_toolbox'),
                         'launch', 'online_async_launch.py')
        ),
        launch_arguments={'slam_params_file': slam_params,
                           'use_sim_time': 'true'}.items()
    )

    rviz = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', os.path.join(pkg_path, 'rviz', 'config.rviz')],
        output='screen'
    )

    return LaunchDescription([slam_toolbox, rviz])
