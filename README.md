# ROS2 Autonomous Navigation and Obstacle Avoidance Rover System
An ROS2-based autonomous robotic rover system that avoids obstacles using simulated sensors. The system publishes odometry and transforms and visualises its behavior in RViz. The project also produces simulated motor control using a C++ node that prints to the terminal. 

## Demo media
![Robot Demo](media/demo_small.gif)

## Overview
This project shows a complete robotics pipeline that was built with ROS2, including:
- Multi-sensor perception
- Reactive obstacle avoidence
- Velocity command generation
- Odometry tracking
- Transform broadcasting
- Real time visualisation in RViz
- Cross-language integration (Python and C++)

The system has been designed to be easily extendable and can be launched with a single command.

## System architecture
Sensors (Python) -> Controller (Python) -> /Cmd_vel -> Motor Node (C++) -> Odometry Node (Python) -> /odom + /tf -> RViz

## Features
- Parametarised sensor nodes
- Obstacle avoidance logic (using multi-directional sensing)
- Dynamic TF broadcasting
- Odometry-based path tracking
- RViz visualisation with:
	- Simple robot model (URDF)
	- TF tree
	- Odometry trail
- Launch file for single command execution

## Demo
Run the system:#

cd ~/ros2_ws
colcon build
source install/setup.bash
ros2 launch navigation_robot demo.launch.py

## Expected behavior
- Rover moves forward autonomously
- Simulated sensors detect obstacle
- Either turns or stops based on sensor reading
- Leaves a visable trajectory/trail in RViz

## Visualisation
System used RViz for real time feedback:
- RobotModel -> displays UDRF robot
- TF -> shows the frame relationships
- Odometry -> displays movement trail

## Technologies used
- ROS2 (rclpy, rclcpp)
- Python (control, sensing, odometry and logging)
- C++ (motor simulation)
- RViz (visualisation)
- URDF (robot model)

## Design Highlight
Reusable sensor node:

Using ROS2 parameters, a single sensor node is used multiple times, once for each directional sensor. This enables a scalable multi sensor setup without duplicating code. 

## Future improvements
- Visualised arrows for sensors so that obstacle distance can clearly be seen in RViz simulation
- Sensor noise simulation
- Object tracking
- SLAM integration
