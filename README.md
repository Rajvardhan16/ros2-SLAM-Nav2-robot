# 🤖 ROS 2 SLAM & Nav2 Robot

A ROS 2-based **four-wheel differential-drive mobile robot** implementing **LiDAR-based SLAM and autonomous navigation using Nav2**.

The project demonstrates a complete mobile robotics workflow:

**Robot Modeling → Gazebo Simulation → LiDAR → SLAM → RViz → Teleoperation → Map Saving → Nav2 Autonomous Navigation**

---

# 📌 Project Overview

This project develops a four-wheel mobile robot using ROS 2.

The robot is modeled using **URDF/Xacro**, simulated in **Gazebo**, equipped with a **LiDAR sensor**, and controlled using ROS 2 Control.

During the mapping phase, the robot is manually operated using `teleop_twist_keyboard`. LiDAR data is processed by SLAM to generate an occupancy-grid map.

After the map is generated and saved, the robot can use **Nav2** for autonomous navigation.

---

# 🎯 Objectives

* Build a four-wheel mobile robot model in ROS 2.
* Create the robot description using URDF/Xacro.
* Integrate a LiDAR sensor.
* Simulate the robot in Gazebo.
* Implement SLAM-based environment mapping.
* Visualize the robot and map using RViz2.
* Teleoperate the robot during mapping.
* Save the generated map.
* Configure Nav2 for autonomous navigation.
* Test autonomous navigation using the generated map.

---

# ✨ Features

* Four-wheel mobile robot
* Differential-drive motion
* LiDAR-based environment sensing
* Gazebo simulation
* SLAM mapping
* RViz2 visualization
* ROS 2 Control
* Keyboard teleoperation
* Map generation and saving
* Nav2 autonomous navigation
* Configurable robot controllers
* Configurable SLAM parameters
* Configurable Nav2 parameters
* Saved occupancy map

---

# 🏗️ System Architecture

```text
                       ┌──────────────────────┐
                       │    Four-Wheel Robot  │
                       └──────────┬───────────┘
                                  │
                                  ▼
                       ┌──────────────────────┐
                       │       Gazebo         │
                       │     Simulation       │
                       └──────────┬───────────┘
                                  │
                                  ▼
                       ┌──────────────────────┐
                       │        LiDAR         │
                       │   Environment Scan   │
                       └──────────┬───────────┘
                                  │
                                  ▼
                       ┌──────────────────────┐
                       │    SLAM Toolbox      │
                       │    Mapping System    │
                       └──────────┬───────────┘
                                  │
                                  ▼
                       ┌──────────────────────┐
                       │      Occupancy       │
                       │        Map           │
                       └──────────┬───────────┘
                                  │
                                  ▼
                       ┌──────────────────────┐
                       │        Nav2          │
                       │ Navigation Framework │
                       └──────────┬───────────┘
                                  │
                                  ▼
                       ┌──────────────────────┐
                       │ Autonomous Navigation│
                       └──────────────────────┘
```

---

# 🔄 Complete Workflow

```text
                    MAPPING PHASE

        ┌────────────────────────────┐
        │      Start Gazebo          │
        └─────────────┬──────────────┘
                      ▼
        ┌────────────────────────────┐
        │       Start SLAM           │
        └─────────────┬──────────────┘
                      ▼
        ┌────────────────────────────┐
        │          RViz2             │
        │  Visualize Robot + /map    │
        └─────────────┬──────────────┘
                      ▼
        ┌────────────────────────────┐
        │       Teleoperate          │
        │       the Robot            │
        └─────────────┬──────────────┘
                      ▼
        ┌────────────────────────────┐
        │       Generate Map         │
        └─────────────┬──────────────┘
                      ▼
        ┌────────────────────────────┐
        │         Save Map            │
        └─────────────┬──────────────┘
                      │
                      ▼
                 NAVIGATION
                    PHASE

        ┌────────────────────────────┐
        │         Start Nav2         │
        └─────────────┬──────────────┘
                      ▼
        ┌────────────────────────────┐
        │     Localization +         │
        │      Path Planning         │
        └─────────────┬──────────────┘
                      ▼
        ┌────────────────────────────┐
        │    Autonomous Navigation   │
        └────────────────────────────┘
```

---

# 🧰 Technologies

| Technology    | Role                   |
| ------------- | ---------------------- |
| ROS 2         | Robot middleware       |
| Gazebo        | Simulation             |
| SLAM Toolbox  | Mapping                |
| Nav2          | Autonomous navigation  |
| RViz2         | Visualization          |
| ROS 2 Control | Robot control          |
| LiDAR         | Environment perception |
| URDF/Xacro    | Robot modeling         |
| YAML          | Configuration          |
| SDF           | Gazebo world           |

---

# 📦 ROS 2 Package

The repository contains the ROS 2 package:

```text
four_wheel
```

The package contains the robot description, simulation, LiDAR, controllers, SLAM configuration, Nav2 configuration, RViz configurations, and launch files.

---

# 📁 Project Structure

```text
ros2-SLAM-Nav2-robot/
│
├── .gitignore
├── CMakeLists.txt
├── package.xml
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
├── worlds/
│   ├── empty_world.sdf
│   └── maps/
│       ├── my_map.pgm
│       └── my_map.yaml
│
├── include/
└── src/
```

---

# 🤖 Robot Model

The robot is described using Xacro files located in:

```text
urdf/
```

### Robot description files

```text
robot.urdf.xacro
robot_core.xacro
ros2_control.xacro
inertial_macros.xacro
lidar.xacro
```

The Xacro files define the robot structure, inertial properties, LiDAR, and ROS 2 Control integration.

---

# 📡 LiDAR

The LiDAR description is located at:

```text
urdf/lidar.xacro
```

The LiDAR provides environmental scan data used during SLAM mapping.

The LiDAR allows the robot to detect surrounding walls and obstacles while moving through the simulated environment.

---

# ⚙️ ROS 2 Control

The robot uses ROS 2 Control for its drive controller.

The controller configuration is:

```text
config/my_controllers.yaml
```

The robot's ROS 2 Control interface is defined through:

```text
urdf/ros2_control.xacro
```

The teleoperation command publishes velocity commands to:

```text
/diff_drive_controller/cmd_vel
```

---

# 🌍 Gazebo Simulation

The project includes a Gazebo simulation environment.

### World

```text
worlds/empty_world.sdf
```

### Launch file

```text
launch/gazebo.launch.py
```

Gazebo provides the simulated robot, environment, sensors, and controllers.

---

# 🗺️ SLAM

SLAM is used to construct an occupancy-grid map while the robot explores the environment.

### SLAM configuration

```text
config/mapper_params_online_async.yaml
```

### SLAM launch file

```text
launch/slam.launch.py
```

The robot is manually driven during mapping so that the LiDAR can scan different areas of the environment.

---

# 🖥️ RViz2 Configuration

RViz2 is used to visualize the robot, TF frames, LiDAR information, and generated map.

The repository contains:

```text
rviz/
├── nav.rviz
└── rviz_config.rviz
```

---

## Starting RViz2

Open a new terminal:

```bash
source ~/ros2_ws/install/setup.bash
```

Then:

```bash
rviz2
```

---

# ⚙️ RViz2 Settings for SLAM

For the mapping stage, configure RViz2 as follows.

## 1. Set Fixed Frame

In the **Global Options** panel:

```text
Fixed Frame → map
```

The fixed frame should be:

```text
map
```

This is the required frame for viewing the generated SLAM map.

---

## 2. Add Map Display

In RViz2:

```text
Add
  ↓
By topic
  ↓
/map
```

Select the `/map` topic to display the occupancy-grid map.

The map should update as the robot moves through the environment.

---

## 3. Map QoS Settings

If RViz2 displays:

```text
No map received
```

open the **Map display's QoS settings**.

Set:

```text
Reliability  → Reliable
Durability   → Transient Local
```

These are the QoS settings specified in the project's current SLAM workflow.

---

## 4. Recommended RViz Displays

For a useful mapping visualization, the RViz configuration can include:

```text
Map
TF
RobotModel
LaserScan
Odometry
```

The essential SLAM configuration documented for this project is:

```text
Fixed Frame → map
Map Topic   → /map
```

with the Map QoS settings above when necessary.

---

# 🎮 Robot Teleoperation

During mapping, the robot is manually controlled using:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -p stamped:=true -p frame_id:=base_link -r cmd_vel:=/diff_drive_controller/cmd_vel
```

The command publishes the robot velocity command to:

```text
/diff_drive_controller/cmd_vel
```

and uses:

```text
frame_id → base_link
```

The robot should be driven around the environment so that SLAM can observe the surroundings.

---

# 💾 Saving the Map

After sufficiently exploring the environment, save the generated map using:

```bash
ros2 run nav2_map_server map_saver_cli -f ~/ros2_ws/maps/my_map
```

The map is saved using the name:

```text
my_map
```

The repository also contains a saved map:

```text
worlds/maps/
├── my_map.pgm
└── my_map.yaml
```

---

# 🧭 Nav2

Nav2 is used for autonomous navigation after the environment map has been created.

### Nav2 configuration

```text
config/nav2_params.yaml
```

### Navigation launch file

```text
launch/navigation.launch.py
```

The navigation launch file starts the configured navigation system for the robot.

---

# 🚀 Installation

## 1. Create Workspace

```bash
mkdir -p ~/ros2_ws/src
```

## 2. Clone Repository

```bash
cd ~/ros2_ws/src
git clone https://github.com/Rajvardhan16/ros2-SLAM-Nav2-robot.git
```

## 3. Build Package

```bash
cd ~/ros2_ws
colcon build --packages-select four_wheel
```

## 4. Source Workspace

```bash
source install/setup.bash
```

The project command sequence starts with building the `four_wheel` package and sourcing the workspace.

---

# ▶️ COMPLETE EXECUTION

The project is operated in several terminals.

```text
Terminal 1 → Gazebo
Terminal 2 → SLAM
Terminal 3 → RViz2
Terminal 4 → Teleoperation
```

After mapping:

```text
Save Map → Start Nav2
```

---

# 🟢 TERMINAL 1 — Start Gazebo

Open Terminal 1:

```bash
cd ~/ros2_ws
```

Source the workspace:

```bash
source install/setup.bash
```

Launch Gazebo:

```bash
ros2 launch four_wheel gazebo.launch.py
```

Keep this terminal running.

---

# 🗺️ TERMINAL 2 — Start SLAM

Open Terminal 2:

```bash
cd ~/ros2_ws
```

Source:

```bash
source install/setup.bash
```

Launch SLAM:

```bash
ros2 launch four_wheel slam.launch.py
```

Keep this terminal running.

---

# 🖥️ TERMINAL 3 — Start RViz2

Open Terminal 3:

```bash
source ~/ros2_ws/install/setup.bash
```

Launch RViz:

```bash
rviz2
```

Then configure RViz:

### Global Options

```text
Fixed Frame → map
```

### Map

```text
Add → By topic → /map
```

### Map QoS

If:

```text
No map received
```

set:

```text
Reliability → Reliable
Durability → Transient Local
```

---

# 🎮 TERMINAL 4 — Teleoperate Robot

Open Terminal 4:

```bash
source ~/ros2_ws/install/setup.bash
```

Run:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -p stamped:=true -p frame_id:=base_link -r cmd_vel:=/diff_drive_controller/cmd_vel
```

Drive the robot around the environment.

Try to:

* Cover the complete environment.
* Move around corners.
* Avoid moving too quickly.
* Allow the LiDAR to observe different areas.
* Return near previously visited areas when appropriate.

This allows SLAM to build the environment map.

---

# 💾 TERMINAL 5 — Save Map

Once mapping is complete:

```bash
ros2 run nav2_map_server map_saver_cli -f ~/ros2_ws/maps/my_map
```

This saves the map for later navigation.

---

# 🧭 TERMINAL 6 — Start Nav2

After saving the map, open a terminal:

```bash
cd ~/ros2_ws
```

Source:

```bash
source install/setup.bash
```

Launch Nav2:

```bash
ros2 launch four_wheel navigation.launch.py
```

Nav2 can then be used for autonomous navigation using the configured navigation system.

---

# 🔄 Mapping Sequence

```text
1. Build Package
       ↓
2. Start Gazebo
       ↓
3. Start SLAM
       ↓
4. Start RViz
       ↓
5. Set Fixed Frame = map
       ↓
6. Add /map
       ↓
7. Start Teleoperation
       ↓
8. Drive Robot
       ↓
9. Build Map
       ↓
10. Save Map
```

---

# 🧭 Navigation Sequence

```text
             Saved Map
                 │
                 ▼
        ┌──────────────────┐
        │      Nav2        │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │  Localization    │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │  Global Planner  │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │  Local Planner   │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │   Controller     │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ Four-Wheel Robot │
        └──────────────────┘
```

---

# ⚙️ Configuration Files

## Controller

```text
config/my_controllers.yaml
```

Used for robot controller configuration.

## SLAM

```text
config/mapper_params_online_async.yaml
```

Used for SLAM configuration.

## Nav2

```text
config/nav2_params.yaml
```

Used for Nav2 navigation configuration.

---

# 🚀 Launch Files

| File                   | Function                 |
| ---------------------- | ------------------------ |
| `gazebo.launch.py`     | Launch Gazebo simulation |
| `slam.launch.py`       | Start SLAM               |
| `navigation.launch.py` | Start Nav2               |
| `rsp.launch.py`        | Robot State Publisher    |

---

# 🖥️ RViz Files

```text
rviz/
├── nav.rviz
└── rviz_config.rviz
```

These configurations provide RViz visualization setups for the robot and navigation workflow.

---

# 🗺️ Map Files

The repository contains:

```text
worlds/maps/
├── my_map.pgm
└── my_map.yaml
```

The `.pgm` file contains the occupancy-grid image and the `.yaml` file provides the associated map metadata.

---

# 🧪 Testing

The system can be tested in the following order:

### 1. Gazebo

Verify:

* Robot appears correctly.
* Wheels respond to commands.
* LiDAR is active.

### 2. SLAM

Verify:

* SLAM starts correctly.
* LiDAR scans the environment.
* `/map` is generated.

### 3. RViz

Verify:

```text
Fixed Frame → map
```

and:

```text
/map
```

is visible.

### 4. Teleoperation

Verify the robot responds to keyboard commands.

### 5. Map Saving

Verify that the map is saved successfully.

### 6. Nav2

Verify that the saved map can be used for autonomous navigation.

---

# 🛠️ Development

After modifying the package:

```bash
cd ~/ros2_ws
```

Build:

```bash
colcon build --packages-select four_wheel
```

Source:

```bash
source install/setup.bash
```

Then restart the required launch files.

---

# 📚 Learning Outcomes

This project provides practical experience with:

* ROS 2
* Mobile robotics
* Four-wheel robot modeling
* Differential-drive systems
* URDF/Xacro
* ROS 2 Control
* Gazebo
* LiDAR
* SLAM
* Occupancy-grid mapping
* RViz2
* Nav2
* Localization
* Path planning
* Autonomous navigation
* Robot teleoperation
* Map generation
* Map saving

---

# 🔮 Future Improvements

* Autonomous exploration
* Improved localization
* Waypoint navigation
* Dynamic obstacle avoidance
* Multiple sensor integration
* Depth camera integration
* Improved controller tuning
* Real hardware implementation
* Hardware-in-the-loop testing
* Autonomous map exploration
* Multi-goal navigation

---

# 📸 Demo

Recommended screenshots/videos for this repository:

### 1. Gazebo

Four-wheel robot operating in the simulated environment.

### 2. LiDAR

LiDAR scan around the robot.

### 3. SLAM

Live `/map` generation in RViz2.

### 4. Completed Map

Final occupancy-grid map.

### 5. Nav2

Robot navigating autonomously using the saved map.

---

# 👨‍💻 Author

**Rajvardhan**

Robotics & Automation Engineering

GitHub: **Rajvardhan16**

---

# ⭐ Repository

If this project is useful for learning ROS 2, SLAM, Nav2, or mobile robotics, consider giving the repository a ⭐.

**Repository:** `ros2-SLAM-Nav2-robot`

---

## 📄 License

License information will be added as the project develops.
