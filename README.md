# Aero Path Planner

Implements A* and B-Spline trajectory smoothing on simulated 2D/3D grid maps. Designed to benchmark the performance of ESDF-based planning modules under voxel constraints. Currently simulating drone-like movement dynamics.

# aero_path_planner

> 3D A* Planning with B-Spline Trajectory Optimization for Autonomous Aerial Navigation

This repository implements a hybrid path planning pipeline designed for autonomous aerial vehicles navigating in voxelized 3D environments. It combines grid-based A* search (with optional 8-direction Hybrid-A*) and B-spline trajectory smoothing to generate dynamically feasible paths under voxel and obstacle constraints.

The project simulates drone-like dynamics and emphasizes ESDF-integrated planning pipelines. It is intended as a lightweight research-grade toolkit for benchmarking and experimentation.

## 🧠 Key Concepts

- Discrete path planning using A* or Hybrid-A* in voxelized 3D maps
- B-spline curve optimization via `scipy.interpolate` for smoothing raw paths
- Euclidean Signed Distance Field (ESDF)-friendly design, compatible with Voxblox-style maps
- Designed for extensibility toward kinodynamic planning and trajectory tracking

## ✨ Features

- ✅ 3D grid map representation with 6/8/26-neighbour A* search
- ✅ B-spline or cubic smoothing for trajectory continuity and feasibility
- ✅ Visual debugging support using `matplotlib` or optional `RViz` dump
- ✅ Modular design for plugging into control pipelines or benchmark suites

## 📦 Applications

- Drone path planning in indoor/outdoor 3D environments
- Research on map-aware motion planning with obstacle proximity constraints
- Integration into larger autonomy stacks (mapping + planning + control)

## 📂 Structure
```
aero_path_planner/
├── astar/ # Grid-based A* and hybrid path planning
├── smoothing/ # B-spline smoothing and curve evaluation
├── map/ # Grid or ESDF map simulation
├── test/ # Unit tests and simulation scenes
├── visualization/ # Matplotlib-based visualization utilities
├── scripts/ # Demo runners
├── requirements.txt
└── README.md
```

## 🛠️ Installation

```bash
pip install -r requirements.txt
```
