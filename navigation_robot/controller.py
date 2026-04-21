import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist

class controller(Node):
	def __init__(self):
		super().__init__('controller_node')
		self.subscription = self.create_subscription(
			Float32,
			'distance',
			self.check_distance,
			10
		)

		self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)

	def check_distance(self, msg):
		distance = msg.data
		cmd = Twist()

		speed = max(0.0, min(1.0, distance / 100.0))

		cmd.linear.x = speed

		self.get_logger().info(f"Distance: {distance:.2f} -> Speed: {speed:.2f}")

		self.publisher.publish(cmd)

		#if distance < 20.0:
		#	self.get_logger().info("STOP - Object too close")
		#	command_msg.data = "STOP"
		#	self.publisher.publish(command_msg)
		#elif distance < 50.0:
		#	self.get_logger().info("Reduce speed - aproaching object")
		#	command_msg.data = "Reduce speed"
		#	self.publisher.publish(command_msg)
		#else:
		#	self.get_logger().info("Top speed - Path clear")
		#	command_msg.data = "Top speed"
		#	self.publisher.publish(command_msg)

def main(args=None):
	rclpy.init(args=args)
	node = controller()
	rclpy.spin(node)
	node.destroy_node()
	rclpy.shutdown()
