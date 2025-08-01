import rcply

from rcply.node import Node

import time 

class HelloWorldNode(Node):
    
    def _init_(self):
      # call the constructor if the based class Node to set the node name.

       super()._init_('hello_world_demo')


    def run(self):
       # Execute a loop when the ROS2 system is running normally

         while rclpy.ok():
            #print "Hello World" to the node's log.

            self.get_logger().info('Hello World')

            # Sleep for 0.5s to control the loop time
            time.sleep(0.5)



def main(args=None):
    # Initialize ROS2 Python interface
    rclpy.init(args=args)
    # Create an instance of HelloWorldNode

    node = HelloWorldNode()


    try:
        # Run the main loop of the node.

        node.run()

    except KeyboardInterrupt:
        pass

    finally:
        # Destroy the node object

        node.destroy_node()

        # Shut down ROS2 Python interface

        rclpy.shutdown()


if __name__ == '__main__':
   
    # Execute the main function
   
   main()


