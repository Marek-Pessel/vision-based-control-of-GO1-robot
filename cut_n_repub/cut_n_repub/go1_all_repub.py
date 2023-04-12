import rclpy # Python library for ROS 2
from rclpy.node import Node # Handles the creation of nodes
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library

class ImageRePublisher(Node):
  """
  Create an ImageRePublisher class, which divides Go1's cams into two topics (left and right).
  """
  def __init__(self):
    """
    Class constructor to set up the node
    """
    # Initiate the Node class's constructor and give it a name
    super().__init__('go1_all_repub')

    # Create the subscriber.
    self.front_subscription = self.create_subscription(Image, 'cam_front/image_raw', self.front_listener_callback, 10)
    self.front_subscription # prevent unused variable warning

    self.chin_subscription = self.create_subscription(Image, 'cam_chin/image_raw', self.chin_listener_callback, 10)
    self.chin_subscription # prevent unused variable warning

    self.left_subscription = self.create_subscription(Image, 'cam_left/image_raw', self.left_listener_callback, 10)
    self.left_subscription # prevent unused variable warning

    self.right_subscription = self.create_subscription(Image, 'cam_right/image_raw', self.right_listener_callback, 10)
    self.right_subscription # prevent unused variable warning

    self.abdomen_subscription = self.create_subscription(Image, 'cam_abdomen/image_raw', self.abdomen_listener_callback, 10)
    self.abdomen_subscription # prevent unused variable warning

    # Create the publishers.
    self.front_publisher_left = self.create_publisher(Image, 'front_camera/left/image_raw', 10)
    self.front_publisher_right = self.create_publisher(Image, 'front_camera/right/image_raw', 10)

    self.chin_publisher_left = self.create_publisher(Image, 'chin_camera/left/image_raw', 10)
    self.chin_publisher_right = self.create_publisher(Image, 'chin_camera/right/image_raw', 10)

    self.left_publisher_left = self.create_publisher(Image, 'left_camera/left/image_raw', 10)
    self.left_publisher_right = self.create_publisher(Image, 'left_camera/right/image_raw', 10)

    self.right_publisher_left = self.create_publisher(Image, 'right_camera/left/image_raw', 10)
    self.right_publisher_right = self.create_publisher(Image, 'right_camera/right/image_raw', 10)

    self.abdomen_publisher_left = self.create_publisher(Image, 'abdomen_camera/left/image_raw', 10)
    self.abdomen_publisher_right = self.create_publisher(Image, 'abdomen_camera/right/image_raw', 10)

    # Used to convert between ROS and OpenCV images
    self.br = CvBridge()


  def front_listener_callback(self, data):
    """
    Callback function.
    """
    # Convert ROS Image message to OpenCV image
    current_frame = self.br.imgmsg_to_cv2(data, desired_encoding='bgr8')

    #cut in half
    h, w, channels = current_frame.shape  
    half = w//2
    left_part = current_frame[:, :half]
    right_part = current_frame[:, half:]

    # Publish to new topic
    self.front_publisher_left.publish(self.br.cv2_to_imgmsg(left_part))
    self.front_publisher_right.publish(self.br.cv2_to_imgmsg(right_part))

  def chin_listener_callback(self, data):
    """
    Callback function.
    """
    # Convert ROS Image message to OpenCV image
    current_frame = self.br.imgmsg_to_cv2(data, desired_encoding='bgr8')

    #cut in half
    h, w, channels = current_frame.shape  
    half = w//2
    left_part = current_frame[:, :half]
    right_part = current_frame[:, half:]

    # Publish to new topic
    self.chin_publisher_left.publish(self.br.cv2_to_imgmsg(left_part))
    self.chin_publisher_right.publish(self.br.cv2_to_imgmsg(right_part))

  def left_listener_callback(self, data):
    """
    Callback function.
    """
    # Convert ROS Image message to OpenCV image
    current_frame = self.br.imgmsg_to_cv2(data, desired_encoding='bgr8')

    #cut in half
    h, w, channels = current_frame.shape  
    half = w//2
    left_part = current_frame[:, :half]
    right_part = current_frame[:, half:]

    # Publish to new topic
    self.left_publisher_left.publish(self.br.cv2_to_imgmsg(left_part))
    self.left_publisher_right.publish(self.br.cv2_to_imgmsg(right_part))

  def right_listener_callback(self, data):
    """
    Callback function.
    """
    # Convert ROS Image message to OpenCV image
    current_frame = self.br.imgmsg_to_cv2(data, desired_encoding='bgr8')

    #cut in half
    h, w, channels = current_frame.shape  
    half = w//2
    left_part = current_frame[:, :half]
    right_part = current_frame[:, half:]

    # Publish to new topic
    self.right_publisher_left.publish(self.br.cv2_to_imgmsg(left_part))
    self.right_publisher_right.publish(self.br.cv2_to_imgmsg(right_part))

  def abdomen_listener_callback(self, data):
    """
    Callback function.
    """
    # Convert ROS Image message to OpenCV image
    current_frame = self.br.imgmsg_to_cv2(data, desired_encoding='bgr8')

    #cut in half
    h, w, channels = current_frame.shape  
    half = w//2
    left_part = current_frame[:, :half]
    right_part = current_frame[:, half:]

    # Publish to new topic
    self.abdomen_publisher_left.publish(self.br.cv2_to_imgmsg(left_part))
    self.abdomen_publisher_right.publish(self.br.cv2_to_imgmsg(right_part))

def main(args=None):

  # Initialize the rclpy library
  rclpy.init(args=args)

  # Create the nodes
  go1_repub = ImageRePublisher()

  # Spin the node so the callback function is called.
  rclpy.spin(go1_repub)

  # Destroy the nodes explicitly
  # (optional - otherwise it will be done automatically
  # when the garbage collector destroys the node object)
  go1_repub.destroy_node()

  # Shutdown the ROS client library for Python
  rclpy.shutdown()

if __name__ == '__main__':
  main()
