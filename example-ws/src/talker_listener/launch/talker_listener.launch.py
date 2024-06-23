from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='talker_listener',
            # namespace='',
            executable='talkerNode',
            name='talker_node'
        ),
        Node(
            package='talker_listener',
            # namespace='',
            executable='listenerNode',
            name='listener_node'
        ),
        # Node(
        #     package='turtlesim',
        #     executable='mimic',
        #     name='mimic',
        #     remappings=[
        #         ('/input/pose', '/turtlesim1/turtle1/pose'),
        #         ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
        #     ]
        # )
    ])