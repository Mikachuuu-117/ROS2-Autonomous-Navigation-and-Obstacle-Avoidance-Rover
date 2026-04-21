#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"

using std::placeholders::_1;

class MotorNode : public rclcpp::Node
{
public:
	MotorNode() : Node("motor_node")
	{
		subscription_ = this->create_subscription<geometry_msgs::msg::Twist>(
			"cmd_vel",
			10,
			std::bind(&MotorNode::move_robot, this, _1)
		);
	}

private:
	void move_robot(const geometry_msgs::msg::Twist::SharedPtr msg)
	{
		float speed = msg->linear.x;
		float turn = msg->angular.z;

		RCLCPP_INFO(
			this->get_logger(),
			"Speed: %.2f | Turn: %.2f",
			speed,
			turn
		);
	}

	rclcpp::Subscription<geometry_msgs::msg::Twist>::SharedPtr subscription_;
};

int main(int argc, char * argv[])
{
	rclcpp::init(argc, argv);
	rclcpp::spin(std::make_shared<MotorNode>());
	rclcpp::shutdown();
	return 0;
}
