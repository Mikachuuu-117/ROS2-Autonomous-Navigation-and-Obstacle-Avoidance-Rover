import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist

class controller(Node):
	def __init__(self):
		super().__init__('controller_node')

		self.front = 10.0
		self.left = 10.0
		self.right = 10.0

		self.create_subscription(Float32, '/distance_front', self.front_cb, 10)
		self.create_subscription(Float32, '/distance_left', self.left_cb, 10)
		self.create_subscription(Float32, '/distance_right', self.right_cb, 10)

		self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
		self.timer = self.create_timer(1.0, self.control_loop)


	def front_cb(self, msg):
		self.front = msg.data

	def left_cb(self, msg):
		self.left = msg.data

	def right_cb(self, msg):
		self.right = msg.data



	def control_loop(self):
		cmd = Twist()
		cmd.linear.x = 1.0
		cmd.angular.z = 0.0

		if self.front < 0.5:
			cmd.linear.x = 0.0    # Stop if obstacle is straight ahead

		if self.left < 0.5 and self.right < 0.5:
			cmd.linear.x = 0.0    # Stop if an obstacle is close on both sides

		elif self.left < 0.5:
			cmd.angular.z = -0.5  # Turning right

		elif self.right < 0.5:
			cmd.angular.z = 0.5   # Turning left

		self.publisher.publish(cmd)
		self.get_logger().info(
			f"F:{self.front:.2f} L:{self.left:.2f} R:{self.right:.2f} "
			f"| Speed:{cmd.linear.x:.2f} Turn:{cmd.angular.z:.2f}"
		)


def main(args=None):
	rclpy.init(args=args)
	node = controller()
	rclpy.spin(node)
	node.destroy_node()
	rclpy.shutdown()
