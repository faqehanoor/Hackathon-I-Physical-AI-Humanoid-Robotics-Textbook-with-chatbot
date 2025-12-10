
---

# ✅ **Tutorial 10 — Advanced Gazebo Physics & Dynamics**

Save as: `10-gazebo-advanced-physics.md`

```md
---
title: Gazebo Advanced Physics & Dynamics
sidebar_position: 10
---

# Advanced Simulation Physics

Humanoid simulation requires precise physics settings:
- Contact dynamics
- Joint damping/friction
- Center of mass adjustments
- Accurate collision geometry

---

# 🔧 Important Physics Parameters

### 1. ODE / DART / Bullet Engines  
Choose physics engine based on accuracy vs speed.

### 2. Friction

<friction> <ode> <mu>1.0</mu> <mu2>1.0</mu2> </ode> </friction> ```

3. Damping

<damping>0.05</damping>


4. Velocity / Torque Limits
🦿 Balance Tuning

Adjust:

Center of Mass (COM)

ZMP (Zero Moment Point)

Foot contact patches

Exercises

Tune humanoid friction for stable standing.

Simulate slippery surfaces.