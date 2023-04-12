import rclpy # Python library for ROS 2
from rclpy.node import Node # Handles the creation of nodes
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library

class ImageRePublisher(Node):
  """
  Create an ImageRePublisher class, which is a subclass of the Node class.
  """
  def __init__(self):
    """
    Class constructor to set up the node
    """
    # Initiate the Node class's constructor and give it a name
    super().__init__('img_repub')

    # Used to convert between ROS and OpenCV images
    self.br = CvBridge()

    # Create the subscriber.
    self.subscription = self.create_subscription(Image, 'v4l/camera/image_raw', self.listener_callback, 10)
    self.subscription # prevent unused variable warning

    # Create the publisher.
    self.publisher = self.create_publisher(Image, 'camera/image_raw', 10)




  def listener_callback(self, data):
    """
    Callback function.
    """
    # Convert ROS Image message to OpenCV image
    current_frame = self.br.imgmsg_to_cv2(data, desired_encoding='bgr8')

    # Publish to new topic
    self.publisher.publish(self.br.cv2_to_imgmsg(current_frame))


def main(args=None):

  # Initialize the rclpy library
  rclpy.init(args=args)

  # Create the nodes
  img_repub = ImageRePublisher()

  # Spin the node so the callback function is called.
  rclpy.spin(img_repub)

  # Destroy the nodes explicitly
  # (optional - otherwise it will be done automatically
  # when the garbage collector destroys the node object)
  img_repub.destroy_node()

  # Shutdown the ROS client library for Python
  rclpy.shutdown()

if __name__ == '__main__':
  main()
