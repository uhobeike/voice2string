#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import openai
from whisper import voice_to_text
from conf import APIKEY

openai.api_key = APIKEY


class StringPublisher(Node):
    def __init__(self):
        super().__init__('voice2string_node')
        self.publisher_ = self.create_publisher(String, '/voice2string', 10)

    def publish_string(self):
        msg = String()
        msg.data = voice_to_text()
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    string_publisher = StringPublisher()

    string_publisher.publish_string()

    string_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
