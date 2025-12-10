---
title: Advanced ROS 2 — Lifecycle, Actions & Middleware
sidebar_position: 9
---

# Advanced ROS 2 Concepts

This module explores deeper ROS 2 features used in humanoid robots:
- Lifecycle nodes
- Actions for long-running tasks
- DDS middleware tuning
- QoS (Quality of Service) profiles

---

# 🧠 Lifecycle Nodes

Lifecycle nodes allow deterministic startup/shutdown.

### Lifecycle States

Unconfigured → Inactive → Active → Finalized


### Example

```python
from rclpy.lifecycle import LifecycleNode

class MotorController(LifecycleNode):
    def on_activate(self, state):
        self.start_motors()


🎯 Actions for Long-Running Tasks

Used for tasks like:

Walking 10 meters

Picking up an object

Turning the torso

Action Structure

Goal → Feedback → Result

⚙ QoS for Humanoids

Critical for:

Real-time sensor streaming

Low-latency motor control

Recommended profiles:

Sensor Data QoS

Best Effort

Keep Last = 1

Exercises

Build a lifecycle node for a humanoid arm motor.

Create an action for walking 5 meters.