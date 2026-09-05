# ROS 2 4-Wheel SLAM & Navigation Robot

A complete **ROS 2 mobile robot simulation** implementing **4-wheel differential-drive motion, LiDAR-based SLAM, map generation, RViz visualization, and autonomous navigation using Nav2**.

The project is developed using **ROS 2** and **Gazebo**, with the robot model described using **URDF/Xacro** and controlled through **ROS 2 Control**.

---

## 📌 Project Overview

This project demonstrates the complete workflow of a mobile robot from simulation to autonomous navigation:

**Robot Model → Gazebo → LiDAR → SLAM → Mapping → Map Saving → Nav2 → Autonomous Navigation**

The robot can be manually driven using keyboard teleoperation while SLAM creates a map of the environment. The generated map can then be saved and used by the **Nav2 navigation stack** for autonomous navigation.

---

## ✨ Features

* 4-wheel differential-drive mobile robot
* URDF/Xacro robot description
* LiDAR sensor simulation
* ROS 2 Control integration
* Gazebo simulation
* Keyboard teleoperation
* SLAM using LiDAR
* Real-time map generation
* RViz visualization
* RobotModel visualization in RViz
* TF visualization
* LaserScan visualization
* Odometry visualization
* Map saving
* Nav2 autonomous navigation
* Saved map support
* Configurable controllers and navigation parameters

---

## 🧠 System Workflow

```text
                 ┌──────────────────┐
                 │   Robot Model    │
                 │    URDF/Xacro    │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │     Gazebo       │
                 │    Simulation    │
                 └────────┬─────────┘
                          │
             ┌────────────┴────────────┐
             │                         │
             ▼                         ▼
      ┌──────────────┐          ┌──────────────┐
      │    LiDAR     │          │ ROS 2 Control│
      └──────┬───────┘          └──────┬───────┘
             │                         │
             ▼                         ▼
      ┌──────────────┐          ┌──────────────┐
      │    SLAM      │          │   Drive      │
      │  Toolbox     │          │ Controller   │
      └──────┬───────┘          └──────┬───────┘
             │                         │
             ▼                         │
      ┌──────────────┐                 │
      │     Map      │                 │
      │  /map topic  │                 │
      └──────┬───────┘                 │
             │                         │
             ▼                         ▼
      ┌────────────────────────────────────┐
      │               RViz                 │
      │ Map + RobotModel + TF + LaserScan │
      └──────────────────┬─────────────────┘
                         │
                         ▼
                  ┌─────────────┐
                  │ Save Map    │
                  └──────┬──────┘
                         │
                         ▼
                  ┌─────────────┐
                  │    Nav2     │
                  │ Navigation  │
                  └──────┬──────┘
                         │
                         ▼
                  Autonomous Robot
```

---

# 🛠️ Technologies Used

| Technology    | Purpose                       |
| ------------- | ----------------------------- |
| ROS 2         | Robot middleware              |
| Gazebo        | Robot simulation              |
| URDF/Xacro    | Robot modeling                |
| ROS 2 Control | Hardware/controller interface |
| LiDAR         | Environment sensing           |
| SLAM Toolbox  | Mapping and localization      |
| RViz2         | Visualization                 |
| Nav2          | Autonomous navigation         |
| Python        | Launch/configuration support  |
| CMake         | ROS 2 package build system    |

---

# 📁 Project Structure

```text
four_wheel/
│
├── CMakeLists.txt
├── package.xml
│
├── commands slam & Nav2 .txt
│
├── config/
│   ├── mapper_params_online_async.yaml
│   ├── my_controllers.yaml
│   └── nav2_params.yaml
│
├── launch/
│   ├── gazebo.launch.py
│   ├── navigation.launch.py
│   ├── rsp.launch.py
│   └── slam.launch.py
│
├── rviz/
│   ├── nav.rviz
│   └── rviz_config.rviz
│
├── urdf/
│   ├── inertial_macros.xacro
│   ├── lidar.xacro
│   ├── robot_core.xacro
│   ├── robot.urdf.xacro
│   └── ros2_control.xacro
│
└── worlds/
    ├── empty_world.sdf
    └── maps/
        ├── my_map.pgm
        └── my_map.yaml
```

---

# 💻 Requirements

Recommended environment:

* Ubuntu
* ROS 2 Jazzy
* Gazebo
* RViz2
* SLAM Toolbox
* Nav2
* `teleop_twist_keyboard`

Make sure ROS 2 is installed and sourced before running the project.

---

# 🚀 Installation

Clone the repository into your ROS 2 workspace:

```bash
cd ~/ros2_ws/src

git clone https://github.com/Rajvardhan16/ros2-SLAM-Nav2-robot.git
```

Go back to the workspace:

```bash
cd ~/ros2_ws
```

Build the package:

```bash
colcon build --packages-select four_wheel
```

Source the workspace:

```bash
source install/setup.bash
```

The project commands use the same build/source workflow as the supplied project command file.

---

# 🤖 Running the Project

## Step 1 — Build the Package

Open a terminal:

```bash
cd ~/ros2_ws
colcon build --packages-select four_wheel
source install/setup.bash
```

---

# 🌍 Step 2 — Start Gazebo

Open **Terminal 1**:

```bash
cd ~/ros2_ws
source install/setup.bash
ros2 launch four_wheel gazebo.launch.py
```

This starts the Gazebo simulation with the 4-wheel robot.

The exact Gazebo launch command is provided in the project command file.

---

# 🗺️ Step 3 — Start SLAM

Open **Terminal 2**:

```bash
cd ~/ros2_ws
source install/setup.bash
ros2 launch four_wheel slam.launch.py
```

This starts the SLAM system and allows the robot to generate a map using its LiDAR.

---

# 👁️ Step 4 — Start RViz2

Open **Terminal 3**:

```bash
source ~/ros2_ws/install/setup.bash
rviz2
```

---

# 🎛️ RViz2 Configuration

RViz is used to visualize:

* Generated map
* Robot model
* LiDAR data
* TF frames
* Robot odometry

## 4.1 Set Fixed Frame

In the **Displays** panel:

```text
Global Options
└── Fixed Frame → map
```

Set:

```text
Fixed Frame = map
```

This is important because the SLAM map is referenced from the `map` frame.

---

# 🗺️ 4.2 Add Map

Click:

```text
Add
→ By display type
→ Map
```

Set:

```text
Topic → /map
```

The project command file specifically uses `/map` for the Map display.

### If RViz shows:

```text
No map received
```

Open the **Map** display settings and set:

```text
Reliability → Reliable
Durability → Transient Local
```

These QoS settings are included in the project's original RViz instructions.

---

# 🤖 4.3 Add RobotModel

To display the actual robot model in RViz:

```text
Add
→ By display type
→ RobotModel
```

Set:

```text
Description Topic → /robot_description
```

Recommended settings:

```text
Visual Enabled → True
Collision Enabled → False
TF Prefix → leave empty
```

You should now see the **4-wheel robot model** inside RViz.

The RobotModel display uses the robot description generated from the URDF/Xacro files.

---

# 🔗 4.4 Add TF

Click:

```text
Add
→ By display type
→ TF
```

TF allows you to visualize the robot's coordinate frames.

You should see frames such as:

```text
map
  ↓
odom
  ↓
base_link
  ↓
laser / lidar frame
  ↓
wheel frames
```

The exact frame names can depend on the robot's URDF/Xacro configuration.

---

# 📡 4.5 Add LaserScan

Click:

```text
Add
→ By display type
→ LaserScan
```

Set:

```text
Topic → /scan
```

This displays the LiDAR measurements around the robot.

You should see laser points appearing around obstacles and walls.

---

# 🛞 4.6 Add Odometry

Click:

```text
Add
→ By display type
→ Odometry
```

Select the available odometry topic generated by the robot's controller.

This allows you to visualize the estimated robot movement.

---

# ✅ Recommended RViz Display Configuration

Your RViz Displays panel should contain approximately:

```text
Displays
│
├── Global Options
│   └── Fixed Frame → map
│
├── Grid
│
├── Map
│   └── Topic → /map
│
├── RobotModel
│   └── Description Topic → /robot_description
│
├── TF
│
├── LaserScan
│   └── Topic → /scan
│
└── Odometry
```

The most important displays for this project are:

```text
Map
RobotModel
TF
LaserScan
Odometry
```

---

# 🎮 Step 5 — Operate the Robot

Open **Terminal 4**:

```bash
source ~/ros2_ws/install/setup.bash

ros2 run teleop_twist_keyboard teleop_twist_keyboard \
--ros-args \
-p stamped:=true \
-p frame_id:=base_link \
-r cmd_vel:=/diff_drive_controller/cmd_vel
```

This starts keyboard control of the robot.

The command is configured to publish the velocity commands to:

```text
/diff_drive_controller/cmd_vel
```

---

# 🎮 Teleoperation Keys

The `teleop_twist_keyboard` node provides keyboard-based movement.

Typical controls include:

```text
        U    I    O

        J    K    L

        M    ,    .
```

Use the corresponding keys shown by the teleoperation node in your terminal.

Drive the robot around the simulated environment.

---

# 🧭 Step 6 — Create the Map

While SLAM is running:

1. Start Gazebo.
2. Start SLAM.
3. Start RViz.
4. Set `Fixed Frame = map`.
5. Add `/map`.
6. Add `RobotModel`.
7. Add `TF`.
8. Add `/scan`.
9. Start teleoperation.
10. Drive the robot around the environment.

As the robot moves, SLAM builds the map.

RViz should show something similar to:

```text
             Generated Map
    ┌──────────────────────────┐
    │                          │
    │     █████████            │
    │     █       █            │
    │     █   🤖  █            │
    │     █       █            │
    │     █████████            │
    │                          │
    └──────────────────────────┘
```

The robot should gradually explore the environment and generate the occupancy grid.

---

# 💾 Step 7 — Save the Map

After completing the mapping process, open another terminal:

```bash
ros2 run nav2_map_server map_saver_cli -f ~/ros2_ws/maps/my_map
```

This saves the map as:

```text
my_map.pgm
my_map.yaml
```

The project's supplied command file uses this exact map-saving command.

---

# 🧭 Step 8 — Start Nav2

After creating/saving the map, start the navigation system.

Open a new terminal:

```bash
cd ~/ros2_ws
source install/setup.bash
ros2 launch four_wheel navigation.launch.py
```

Nav2 uses the saved map together with the robot's sensors, transforms, odometry, and navigation configuration to perform autonomous navigation.

---

# 🧠 SLAM vs Nav2

## SLAM Mode

SLAM is used when the environment is unknown.

```text
LiDAR
  ↓
SLAM
  ↓
Map
  ↓
RViz
```

The robot explores the environment and creates a map.

---

## Navigation Mode

After the map is available:

```text
Saved Map
    ↓
  Nav2
    ↓
Localization
    ↓
Path Planning
    ↓
Controller
    ↓
Robot
```

Nav2 uses the map to plan and execute navigation.

---

# ⚙️ Configuration Files

## `config/mapper_params_online_async.yaml`

Contains parameters for the SLAM system.

It controls SLAM-related behavior such as mapping configuration and sensor processing.

---

## `config/my_controllers.yaml`

Contains the robot controller configuration.

It is associated with the ROS 2 Control system and differential-drive controller.

---

## `config/nav2_params.yaml`

Contains configuration parameters for the Nav2 navigation system.

This file is used when running autonomous navigation.

---

# 🚀 Launch Files

## `gazebo.launch.py`

Starts the Gazebo simulation and loads the robot into the simulated environment.

Run:

```bash
ros2 launch four_wheel gazebo.launch.py
```

---

## `slam.launch.py`

Starts the SLAM system.

Run:

```bash
ros2 launch four_wheel slam.launch.py
```

---

## `navigation.launch.py`

Starts the Nav2 navigation system.

Run:

```bash
ros2 launch four_wheel navigation.launch.py
```

---

## `rsp.launch.py`

Starts the robot state publisher / robot description related system used for publishing the robot's TF structure.

---

# 🤖 Robot Description

The robot is defined using Xacro files located inside:

```text
urdf/
```

Important files include:

```text
robot.urdf.xacro
robot_core.xacro
ros2_control.xacro
lidar.xacro
inertial_macros.xacro
```

The Xacro structure makes the robot model modular and easier to maintain.

---

# 📡 LiDAR

The robot contains a simulated LiDAR sensor.

The LiDAR provides range measurements of the surrounding environment.

The data is used by:

```text
LiDAR
  ↓
/scan
  ↓
SLAM
  ↓
/map
```

The LiDAR is also visualized in RViz through the **LaserScan** display.

---

# 🎮 Robot Control

The robot uses a differential-drive controller.

Velocity commands are sent through:

```text
/diff_drive_controller/cmd_vel
```

Keyboard teleoperation publishes commands to this controller using:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard \
--ros-args \
-p stamped:=true \
-p frame_id:=base_link \
-r cmd_vel:=/diff_drive_controller/cmd_vel
```

---

# 🗺️ Saved Map

The repository contains the generated map files:

```text
worlds/
└── maps/
    ├── my_map.pgm
    └── my_map.yaml
```

The `.pgm` file contains the occupancy-grid image.

The `.yaml` file contains the map metadata and configuration required to load the map.

---

# 🔄 Complete Mapping Workflow

For quick reference:

### Terminal 1 — Build

```bash
cd ~/ros2_ws
colcon build --packages-select four_wheel
source install/setup.bash
```

### Terminal 2 — Gazebo

```bash
cd ~/ros2_ws
source install/setup.bash
ros2 launch four_wheel gazebo.launch.py
```

### Terminal 3 — SLAM

```bash
cd ~/ros2_ws
source install/setup.bash
ros2 launch four_wheel slam.launch.py
```

### Terminal 4 — RViz

```bash
source ~/ros2_ws/install/setup.bash
rviz2
```

RViz:

```text
Fixed Frame → map

Add:
→ Map
→ RobotModel
→ TF
→ LaserScan
→ Odometry
```

Map:

```text
Topic → /map
```

RobotModel:

```text
Description Topic → /robot_description
```

LaserScan:

```text
Topic → /scan
```

If `/map` shows **No map received**:

```text
Map
├── Reliability → Reliable
└── Durability → Transient Local
```

### Terminal 5 — Teleoperation

```bash
source ~/ros2_ws/install/setup.bash

ros2 run teleop_twist_keyboard teleop_twist_keyboard \
--ros-args \
-p stamped:=true \
-p frame_id:=base_link \
-r cmd_vel:=/diff_drive_controller/cmd_vel
```

### Save Map

```bash
ros2 run nav2_map_server map_saver_cli -f ~/ros2_ws/maps/my_map
```

### Start Nav2

```bash
cd ~/ros2_ws
source install/setup.bash
ros2 launch four_wheel navigation.launch.py
```

---

# 🧩 Troubleshooting

## 1. Package not found

If you get:

```text
Package 'four_wheel' not found
```

Run:

```bash
cd ~/ros2_ws
colcon build --packages-select four_wheel
source install/setup.bash
```

Then try again.

---

## 2. RViz shows "No map received"

Check:

```text
Fixed Frame → map
```

Then:

```text
Map → Topic → /map
```

Set:

```text
Reliability → Reliable
Durability → Transient Local
```

---

## 3. RobotModel is not visible

Check:

```text
RobotModel
└── Description Topic → /robot_description
```

Also verify that the robot description is being published and that TF is available.

---

## 4. LiDAR is not visible

Add:

```text
LaserScan
```

and select:

```text
/scan
```

Also make sure the LiDAR frame is connected to the robot TF tree.

---

## 5. Robot does not move

Check that the controller is running and that teleoperation is publishing to:

```text
/diff_drive_controller/cmd_vel
```

You can inspect topics using:

```bash
ros2 topic list
```

---

## 6. Check ROS 2 Nodes

```bash
ros2 node list
```

---

## 7. Check ROS 2 Topics

```bash
ros2 topic list
```

---

## 8. Check LiDAR Data

```bash
ros2 topic echo /scan
```

---

## 9. Check Map Topic

```bash
ros2 topic echo /map
```

---

## 10. Check TF

```bash
ros2 run tf2_tools view_frames
```

---

# 📊 Project Architecture

```text
                     ROS 2
                       │
       ┌───────────────┼────────────────┐
       │               │                │
       ▼               ▼                ▼
    Gazebo           SLAM              Nav2
       │               │                │
       ▼               ▼                ▼
    Robot           Mapping        Navigation
       │               │                │
       ├───────┐       │                │
       │       │       │                │
       ▼       ▼       ▼                ▼
   Wheels    LiDAR    /map          Path Planner
       │       │                        │
       │       └──────────┐             │
       │                  ▼             │
       │                 RViz           │
       │                  │             │
       └──────────────────┴─────────────┘
```

---

# 🎯 Project Objectives

1. Develop a simulated 4-wheel mobile robot.
2. Create the robot model using URDF/Xacro.
3. Integrate a simulated LiDAR sensor.
4. Control the robot using ROS 2 Control.
5. Implement keyboard-based teleoperation.
6. Generate an environment map using SLAM.
7. Visualize the robot and map using RViz2.
8. Save the generated map.
9. Configure Nav2 for autonomous navigation.
10. Demonstrate the complete mobile robot navigation pipeline.

---

# 📈 Future Improvements

Possible future extensions:

* Autonomous waypoint navigation
* Improved localization
* Dynamic obstacle avoidance
* Camera integration
* Object detection
* IMU integration
* Sensor fusion
* Real robot hardware implementation
* ROS 2 lifecycle management
* Custom Nav2 behavior trees
* Autonomous exploration
* Multi-sensor SLAM

---

# 📚 Learning Outcomes

This project provides practical experience with:

* ROS 2 package development
* URDF/Xacro
* TF2
* ROS 2 Control
* Differential-drive robots
* LiDAR sensors
* Gazebo simulation
* SLAM
* Occupancy-grid mapping
* RViz2
* Nav2
* Robot localization
* Path planning
* Autonomous navigation
* ROS 2 launch files
* YAML configuration

---

# 👨‍💻 Author

**Rajvardhan**

Robotics & Automation Engineering

GitHub:

[Rajvardhan16/ros2-SLAM-Nav2-robot](https://github.com/Rajvardhan16/ros2-SLAM-Nav2-robot.git?utm_source=chatgpt.com)

---

# ⭐ Project Summary

This project demonstrates a complete ROS 2 navigation pipeline for a **4-wheel differential-drive mobile robot**.

The robot is modeled using **URDF/Xacro**, simulated in **Gazebo**, equipped with a **LiDAR sensor**, and controlled using **ROS 2 Control**. During mapping, **SLAM** generates an occupancy-grid map while the robot is driven using keyboard teleoperation. **RViz2** provides visualization of the map, robot model, TF frames, LiDAR data, and odometry.

After saving the map, **Nav2** can use the generated environment map for autonomous navigation.

```text
URDF/Xacro
     ↓
Gazebo
     ↓
LiDAR + ROS 2 Control
     ↓
SLAM
     ↓
Map
     ↓
RViz2
     ↓
Save Map
     ↓
Nav2
     ↓
Autonomous Navigation
```

**This project covers the fundamental workflow required to develop, simulate, map, visualize, and autonomously navigate a ROS 2 mobile robot.**
