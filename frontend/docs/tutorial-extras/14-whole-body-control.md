---
title: Whole-Body Control Systems
sidebar_position: 14
---

# Whole-Body Control

Robots must coordinate:
- Torso  
- Arms  
- Legs  
- Balance  

---

# 🧠 Control Hierarchy

Task Planner
├─ Posture Control
├─ Balance Control
└─ Joint-level Control


---

# 🦾 Inverse Kinematics (IK)

```python
target_pose = [x, y, z, roll, pitch, yaw]
joint_angles = ik_solver.solve(target_pose)


🦿 Inverse Dynamics (ID)

Compute torques:

τ = M(q) * q̈ + C(q, q̇) + G(q)

Exercises

Implement simple IK for a humanoid arm.

Test a balance controller in simulation.