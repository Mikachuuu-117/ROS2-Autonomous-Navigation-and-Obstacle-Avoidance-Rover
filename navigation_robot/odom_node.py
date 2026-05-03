import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, TransformStamped
from nav_msgs.msg import Odometry
import tf2_ros
import math

class OdomNode(Node):

	def __init__(self):
		super().__init__('odom_node')
		self.subscription = self.create_subscription(
			Twist,
			'/cmd_vel',
			self.cmd_callback,
			10
		)

		self.odom_pub = self.create_publisher(Odometry, '/odom', 10)
		self.tf_broadcaster = tf2_ros.TransformBroadcaster(self)

		self.x = 0.0
		self.y = 0.0
		self.theta = 0.0
		self.v = 0.0
		self.w = 0.0

		self.timer = self.create_timer(0.1, self.update)

	def cmd_callback(self, msg):
		self.v = msg.linear.x
		self.w = msg.angular.z

	def update(self):
		dt = 0.1
		self.theta += self.w * dt
		self.x += self.v * math.cos(self.theta) * dt
		self.y += self.v * math.sin(self.theta) * dt

		odom = Odometry()
		odom.header.stamp = self.get_clock().now().to_msg()
		odom.header.frame_id = 'odom'
		odom.child_frame_id = 'base_link'
		odom.pose.pose.position.x = self.x
		odom.pose.pose.position.y = self.y

		qz = math.sin(self.theta / 2)
		qw = math.cos(self.theta / 2)

		odom.pose.pose.orientation.z = qz
		odom.pose.pose.orientation.w = qw

		self.odom_pub.publish(odom)

		t = TransformStamped()

		t.header.stamp = self.get_clock().now().to_msg()
		t.header.frame_id = 'odom'
		t.child_frame_id = 'base_link'

		t.transform.translation.x = self.x
		t.transform.translation.y = self.y
		t.transform.rotation.z = qz
		t.transform.rotation.w = qw

		self.tf_broadcaster.sendTransform(t)

def main(args=None):
	rclpy.init(args=args)
	node = OdomNode()
	rclpy.spin(node)
	node.destroy_node()
	rclpy.shutdown()
