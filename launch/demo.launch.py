from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	return LaunchDescription([

		Node(
			package='navigation_robot',
			executable='controller',
			name='controller'
		),

		Node(
			package='navigation_robot',
			executable='odom_node',
			name='odom_node'
		),

		Node(
			package='navigation_robot',
			executable='sensor',
			name='front_sensor',
			parameters=[{'direction': 'front'}]
		),

		Node(
			package='navigation_robot',
			executable='sensor',
			name='left_sensor',
			parameters=[{'direction': 'left'}]
		),

		Node(
			package='navigation_robot',
			executable='sensor',
			name='right_sensor',
			parameters=[{'direction': 'right'}]
		),

		Node(
			package='navigation_robot_cpp',
			executable='motor_node',
			name='motor_node'
		),

		Node(
			package='robot_state_publisher',
			executable='robot_state_publisher',
			arguments=['/home/mikachuuu-117/ros2_ws/src/navigation_robot/urdf/robot.urdf']
		),

		Node(
			package='rviz2',
			executable='rviz2',
			name='rviz2',
			arguments=['-d', '/home/mikachuuu-117/ros2_ws/src/navigation_robot/rviz/demo.rviz']
		),
	])
