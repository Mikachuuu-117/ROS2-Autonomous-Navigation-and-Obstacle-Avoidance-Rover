import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class Sensor(Node):
	def __init__(self):
		super().__init__('sensor_node')
		self.publisher = self.create_publisher(Float32, 'distance', 10)
		self.timer = self.create_timer(1.0, self.publish_distance)

	def publish_distance(self):
		msg = Float32()
		msg.data = random.uniform(0, 100)
		self.publisher.publish(msg)
		self.get_logger().info(f"Distance: {msg.data:.2f} cm")

def main(args = None):
	rclpy.init(args=args)
	node = Sensor()
	rclpy.spin(node)
	node.destroy_node()
	rclpy.shutdown()
