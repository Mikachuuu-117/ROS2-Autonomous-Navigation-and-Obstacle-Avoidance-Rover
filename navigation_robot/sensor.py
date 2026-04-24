import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class Sensor(Node):
	def __init__(self):
		super().__init__('sensor_node')
		self.declare_parameter('direction', 'front')
		self.direction = self.get_parameter('direction').value
		topic_name = f"distance_{self.direction}"
		self.publisher = self.create_publisher(Float32, topic_name, 10)
		self.timer = self.create_timer(1.0, self.publish_distance)
		self.get_logger().info(f"{self.direction} sensor started")


	def publish_distance(self):
		msg = Float32()

		if self.direction == "front":
			msg.data = random.uniform(0.2, 2.0)

		elif self.direction == "left":
			msg.data = random.uniform(0.35, 2.5)

		elif self.direction == "right":
			msg.data = random.uniform(0.35, 2.5)

		self.publisher.publish(msg)
		self.get_logger().info(f"{self.direction}: {msg.data:.2f}")

def main(args = None):
	rclpy.init(args=args)
	node = Sensor()
	rclpy.spin(node)
	node.destroy_node()
	rclpy.shutdown()
