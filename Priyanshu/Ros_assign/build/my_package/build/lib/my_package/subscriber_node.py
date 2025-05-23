#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')
        self.subscription = self.create_subscription(
            String,
            'message_topic',
            self.listener_callback,
            10)
        self.get_logger().info('Subscriber node initialized')

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: "{msg.data}"')


def main(args=None):
    rclpy.init(args=args)
    subscriber_node = SubscriberNode()
    
    try:
        rclpy.spin(subscriber_node)
    except KeyboardInterrupt:
        pass
    finally:
        subscriber_node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()