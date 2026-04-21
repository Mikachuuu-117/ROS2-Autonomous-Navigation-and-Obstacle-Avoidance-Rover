import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class Logger(Node):
	def __init__(self):
		super().__init__('logger_node')
		self.subscription = self.create_subscription(
			Float32,
			'distance',
			self.log_distance,
			10
		)

	def log_distance(self, msg):
		distance = msg.data
		self.get_logger().info(f"[LOGGER] Distance recieved: {distance:.2f} cm")

def main(args=None):
	rclpy.init(args=args)
	node = Logger()
	rclpy.spin(node)
	node.destroy_node()
	rclpy.shutdown()
