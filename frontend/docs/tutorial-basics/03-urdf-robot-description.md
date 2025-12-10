


# URDF & Robot Description

URDF describes the **mechanical body structure** of your robot.

---

# 🦾 URDF Structure

robot
├─ links (body parts)
└─ joints (connections)


### Sample URDF

```xml
<link name="base_link" />
<link name="torso" />
<joint name="base_to_torso" type="fixed">
  <parent link="base_link"/>
  <child link="torso"/>
</joint>


 Create a Simple Robot

Head

Body

Right Arm

Left Arm

Legs

Exercises

Build a basic humanoid URDF.

Add collision + visuals.


Summary

URDF is the blueprint for your robot inside ROS 2 and Gazebo.