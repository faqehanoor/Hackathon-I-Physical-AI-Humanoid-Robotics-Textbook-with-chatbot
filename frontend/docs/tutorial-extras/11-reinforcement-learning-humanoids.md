
---

# ✅ **Tutorial 11 — Reinforcement Learning for Humanoid Locomotion**

Save as: `11-reinforcement-learning-humanoids.md`

```md
---
title: Reinforcement Learning for Humanoids
sidebar_position: 11
---

# Reinforcement Learning (RL)

Teach humanoids to walk using RL algorithms:
- PPO
- SAC
- TD3
- Dreamer-V3

---

# 🧠 RL Loop

State → Policy → Action → Reward → Update


---

# 🏃 RL for Walking (Isaac Gym)

Reward Function Example:
```python
reward = forward_velocity - fall_penalty - joint_limit_penalty

🔧 Curriculum Learning

Train:

Standing

Shifting weight

Stepping

Walking

Exercises

Modify reward to improve stability.

Train a turning gait.