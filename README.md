# ROS 2 4-Wheel SLAM & Nav2 Robot

A ROS 2 simulation of a **4-wheel differential-drive robot** using **Gazebo, LiDAR, SLAM Toolbox, RViz2, ROS 2 Control, and Nav2**.

The robot is first driven manually to create a map using SLAM. The saved map is then used by Nav2 for autonomous navigation.

---

## Features

* 4-wheel differential-drive robot
* URDF/Xacro robot model
* LiDAR sensor
* ROS 2 Control
* Gazebo simulation
* SLAM mapping
* RViz2 visualization
* Map saving
* Nav2 autonomous navigation
* Keyboard teleoperation

---

## Project Structure

```text
four_wheel/
├── CMakeLists.txt
├── package.xml
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

# Requirements

* Ubuntu
* ROS 2 Jazzy
* Gazebo
* RViz2
* SLAM Toolbox
* Nav2
* `teleop_twist_keyboard`

---

# Installation

Clone the repository:

```bash
cd ~/ros2_ws/src
git clone https://github.com/Rajvardhan16/ros2-SLAM-Nav2-robot.git
```

Build the package:

```bash
cd ~/ros2_ws
colcon build --packages-select four_wheel
source install/setup.bash
```

---

# 🗺️ 1. Create the Map

You need **4 terminals** for mapping.

## Terminal 1 — Start Gazebo

```bash
cd ~/ros2_ws
source install/setup.bash
ros2 launch four_wheel gazebo.launch.py
```

Leave this terminal running.

---

## Terminal 2 — Start SLAM

```bash
cd ~/ros2_ws
source install/setup.bash
ros2 launch four_wheel slam.launch.py
```

Leave this terminal running.

---

## Terminal 3 — Start RViz

```bash
source ~/ros2_ws/install/setup.bash
rviz2
```

### RViz Settings

Set:

```text
Global Options
└── Fixed Frame → map
```

Add the following displays:

### Map

```text
Add → Map
Topic → /map
```

If the map does not appear:

```text
Map
├── Reliability → Reliable
└── Durability → Transient Local
```

### Robot Model

```text
Add → RobotModel
Description Topic → /robot_description
Visual Enabled → True
```

### TF

```text
Add → TF
```

### LiDAR

```text
Add → LaserScan
Topic → /scan
```

### Odometry

```text
Add → Odometry
```

Your RViz should now show:

```text
Map
RobotModel
TF
LaserScan
Odometry
```

The `/map` topic and its QoS settings follow the project's existing mapping instructions.

---

## Terminal 4 — Control the Robot

```bash
source ~/ros2_ws/install/setup.bash

ros2 run teleop_twist_keyboard teleop_twist_keyboard \
--ros-args \
-p stamped:=true \
-p frame_id:=base_link \
-r cmd_vel:=/diff_drive_controller/cmd_vel
```

Drive the robot around the environment until the complete area is mapped.

---

# 💾 2. Save the Map

First create the map directory:

```bash
mkdir -p ~/ros2_ws/maps
```

Check that SLAM is publishing the map:

```bash
ros2 topic list
```

Make sure `/map` is present.

Then:

```bash
ros2 topic echo /map --once
```

If the map message is received, save it:

```bash
ros2 run nav2_map_server map_saver_cli -f ~/ros2_ws/maps/my_map
```

The map will be saved as:

```text
~/ros2_ws/maps/
├── my_map.pgm
└── my_map.yaml
```

The map-saving command matches the project's existing workflow.

---

# 🧭 3. Start Nav2

After the map has been saved, you can use Nav2.

You can stop the SLAM process and start the navigation system.

## Terminal 1 — Gazebo

If Gazebo is not already running:

```bash
cd ~/ros2_ws
source install/setup.bash
ros2 launch four_wheel gazebo.launch.py
```

## Terminal 2 — Nav2

```bash
cd ~/ros2_ws
source install/setup.bash
ros2 launch four_wheel navigation.launch.py
```

The project uses this launch command for Nav2.

---

# 👁️ 4. RViz for Nav2

If RViz does not open automatically:

```bash
source ~/ros2_ws/install/setup.bash
rviz2
```

Set:

```text
Global Options
└── Fixed Frame → map
```

Add:

```text
Map
RobotModel
TF
LaserScan
Odometry
Path
```

### Map

```text
Topic → /map
```

If required:

```text
Reliability → Reliable
Durability → Transient Local
```

### RobotModel

```text
Description Topic → /robot_description
Visual Enabled → True
```

### LaserScan

```text
Topic → /scan
```

### TF

Add:

```text
TF
```

### Odometry

Add:

```text
Odometry
```

### Path

Add:

```text
Path
```

Select the available Nav2 path topic.

---

# 🎯 5. Navigate the Robot

Once Nav2 and RViz are running:

### Set Robot Position

Click:

```text
2D Pose Estimate
```

Click the robot's position on the map and drag the arrow in the direction the robot is facing.

### Send Navigation Goal

Click:

```text
Nav2 Goal
```

Click the destination on the map and drag to select the desired direction.

Nav2 will calculate a path and drive the robot toward the selected goal.

---

# 🔄 Complete Workflow

```text
1. Build package
       ↓
2. Start Gazebo
       ↓
3. Start SLAM
       ↓
4. Start RViz
       ↓
5. Configure RViz
       ↓
6. Start teleop
       ↓
7. Drive robot and create map
       ↓
8. Create ~/ros2_ws/maps
       ↓
9. Check /map
       ↓
10. Save my_map
       ↓
11. Start Nav2
       ↓
12. Start RViz
       ↓
13. Set 2D Pose Estimate
       ↓
14. Set Nav2 Goal
       ↓
15. Autonomous Navigation
```

---

# 🔧 Useful Commands

Check available ROS 2 topics:

```bash
ros2 topic list
```

Check the map:

```bash
ros2 topic info /map
```

Check map data:

```bash
ros2 topic echo /map --once
```

Check LiDAR:

```bash
ros2 topic echo /scan --once
```

Check running nodes:

```bash
ros2 node list
```

Check TF:

```bash
ros2 run tf2_tools view_frames
```

---

# ⚙️ Configuration

### SLAM

```text
config/mapper_params_online_async.yaml
```

Contains SLAM configuration.

### Controllers

```text
config/my_controllers.yaml
```

Contains robot controller configuration.

### Nav2

```text
config/nav2_params.yaml
```

Contains Nav2 navigation parameters.

---

# 🚀 Launch Files

| File                   | Purpose                      |
| ---------------------- | ---------------------------- |
| `gazebo.launch.py`     | Starts Gazebo simulation     |
| `slam.launch.py`       | Starts SLAM                  |
| `navigation.launch.py` | Starts Nav2                  |
| `rsp.launch.py`        | Starts robot state publisher |

---

# 🤖 Robot Description

The robot is created using Xacro:

```text
urdf/
├── robot.urdf.xacro
├── robot_core.xacro
├── ros2_control.xacro
├── lidar.xacro
└── inertial_macros.xacro
```

The robot contains a 4-wheel differential-drive system and LiDAR sensor.

---

# 🗺️ Mapping

SLAM uses the LiDAR data:

```text
LiDAR
  ↓
/scan
  ↓
SLAM
  ↓
/map
  ↓
RViz
```

The robot is manually driven around the environment while SLAM builds the map.

---

# 🧭 Navigation

Nav2 uses the saved map:

```text
my_map.yaml
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

The robot can then navigate autonomously to a goal selected in RViz.

---


# 🔮 Future Improvements

* Autonomous exploration
* IMU integration
* Camera integration
* Sensor fusion
* Improved localization
* Dynamic obstacle avoidance
* Waypoint navigation
* Real robot implementation

---

# 👨‍💻 Author

**Rajvardhan**

Robotics & Automation Engineering

GitHub:

[Rajvardhan16/ros2-SLAM-Nav2-robot](https://github.com/Rajvardhan16/ros2-SLAM-Nav2-robot.git?utm_source=chatgpt.com)
