

# ROS 2 Fundamentals

ROS 2 is the **nervous system** of modern robots. It manages communication between sensors, controllers, and AI modules.

---

#  ROS 2 Architecture

Nodes ↔ Topics ↔ Services ↔ Actions ↔ Parameters


###  Node  
A program that performs a specific task.

### Topic  
Publish/subscribe communication channel.

### Service  
Request–response interaction.

###  Action  
Long-running tasks (like walking somewhere).

---

#  Create Your First ROS 2 Node

```python
import rclpy
from rclpy.node import Node

class HelloNode(Node):
    def __init__(self):
        super().__init__("hello_node")
        self.get_logger().info("Hello from ROS 2!")

def main():
    rclpy.init()
    node = HelloNode()
    rclpy.spin(node)

main()


Run:
ros2 run my_pkg hello_node

 Exercises

Create a publisher node.

Create a subscriber node.

Summary

ROS 2 is essential for communication in humanoid robotics and Physical AI systems.


---

