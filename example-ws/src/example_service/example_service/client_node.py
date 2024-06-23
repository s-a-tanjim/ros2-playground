import sys

from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node


class MinimalClientAsync(Node):

  def __init__(self):
    super().__init__('minimal_client_async')
    self.cli = self.create_client(AddTwoInts, 'add_two_ints')
    while not self.cli.wait_for_service(timeout_sec=1.0):
      self.get_logger().info('service not available, waiting again...')
    self.req = AddTwoInts.Request()

  def send_request(self, a, b):
    self.req.a = a
    self.req.b = b
    self.future = self.cli.call_async(self.req)
    # rclpy.spin_until_future_complete(self, self.future)
    # return self.future.result()


def main(args=None):
  rclpy.init(args=args)

  minimal_client = MinimalClientAsync()
  response = minimal_client.send_request(int(sys.argv[1]), int(sys.argv[2]))

  while rclpy.ok():
    rclpy.spin_once(minimal_client)
    if minimal_client.future.done():
      try:
        response = minimal_client.future.result()
        minimal_client.get_logger().info(
          'Result of add_two_ints: for %d + %d = %d' %
          (int(sys.argv[1]), int(sys.argv[2]), response.sum))
      except Exception as e:
        minimal_client.get_logger().info(f"Service call failed: {e}")
      break
  

  minimal_client.destroy_node()
  rclpy.shutdown()


if __name__ == '__main__':
  main()