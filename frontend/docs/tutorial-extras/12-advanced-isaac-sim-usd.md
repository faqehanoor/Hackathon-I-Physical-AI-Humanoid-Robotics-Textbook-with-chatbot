
---

# ✅ **Tutorial 12 — Isaac Sim: Advanced USD & Sensor Pipelines**

Save as: `12-advanced-isaac-sim-usd.md`

```md
---
title: Isaac Sim — Advanced USD Workflows
sidebar_position: 12
---

# USD (Universal Scene Description)

Isaac Sim uses USD for:
- Scenes  
- Sensors  
- Robots  
- Materials  

---

# 🧱 USD Structure

World
├─ Humanoid
├─ Cameras
├─ Lights
└─ Colliders


---

# 📸 Sensor Pipelines

Advanced sensors:
- RGB + Depth Cameras  
- LiDAR  
- Segmentation cameras  
- Optical Flow  

### Example (Python API)

```python
from omni.isaac.sensor import Camera
cam = Camera("/World/Humanoid/HeadCam")
cam.set_resolution(1920, 1080)


⚡ RTX & Real Physics

Use GPU for:

Ray tracing

Soft shadows

Realistic materials

Exercises

Add a head-mounted stereo camera.

Export synthetic dataset.