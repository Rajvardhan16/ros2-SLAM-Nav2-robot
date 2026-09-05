# 🤖 ROS 2 SLAM & Nav2 Robot

A ROS 2-based **four-wheel differential-drive mobile robot** implementing **LiDAR-based SLAM mapping and autonomous navigation using Nav2**.

This project demonstrates a complete mobile robotics workflow starting from robot modeling and simulation, followed by SLAM-based map generation and autonomous navigation using the ROS 2 Navigation Stack (Nav2).

---

# 📌 Project Overview

This project implements a four-wheel mobile robot in ROS 2 with a LiDAR sensor for environment perception.

The robot is simulated in **Gazebo** and can be controlled manually using `teleop_twist_keyboard`. The LiDAR data is used with **SLAM Toolbox** to build a map of the environment.

After creating and saving a map, the same robot can use **Nav2** for autonomous navigation.

The overall workflow is:

```text
Robot Model
     │
     ▼
Gazebo Simulation
     │
     ▼
LiDAR Sensor
     │
     ▼
SLAM Toolbox
     │
     ▼
Build Environment Map
     │
     ▼
Save Map
     │
     ▼
Nav2
     │
     ▼
Autonomous Navigation
```

---

# 🎯 Objectives

The main objectives of this project are:

* Develop a four-wheel mobile robot using ROS 2.
* Create the robot model using URDF/Xacro.
* Simulate the robot in Gazebo.
* Integrate a LiDAR sensor.
* Implement SLAM for environment mapping.
* Visualize the generated map in RViz.
* Control the robot using keyboard teleoperation.
* Save the generated map for later use.
* Configure Nav2 for autonomous navigation.
* Test navigation using a previously generated map.

---

# ✨ Features

* 🤖 Four-wheel differential-drive mobile robot
* 🌍 Gazebo simulation
* 📡 LiDAR integration
* 🗺️ SLAM mapping
* 🧭 Nav2 autonomous navigation
* 🎮 Keyboard teleoperation
* 🖥️ RViz visualization
* ⚙️ ROS 2 Control
* 📐 URDF/Xacro robot description
* 🎛️ Configurable controllers
* 🗺️ Saved occupancy map
* 🚀 Separate launch files for simulation, SLAM, and navigation

---

# 🏗️ System Architecture

```text
                  ┌────────────────────┐
                  │    Four-Wheel      │
                  │   Mobile Robot     │
                  └─────────┬──────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │      Gazebo        │
                  │    Simulation      │
                  └─────────┬──────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │       LiDAR        │
                  │  Environment Scan  │
                  └─────────┬──────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │    SLAM Toolbox    │
                  │   Mapping System   │
                  └─────────┬──────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │    Occupancy Map   │
                  └─────────┬──────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │       Nav2         │
                  │ Navigation Stack   │
                  └─────────┬──────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │ Autonomous Robot   │
                  │     Navigation     │
                  └────────────────────┘
```

---

# 🔄 Complete Project Workflow

The project is divided into two major stages.

## Stage 1 — Mapping

```text
Gazebo
  │
  ▼
Robot + LiDAR
  │
  ▼
SLAM Toolbox
  │
  ▼
Manual Teleoperation
  │
  ▼
Explore Environment
  │
  ▼
Generate Map
  │
  ▼
Save Map
```

## Stage 2 — Navigation

```text
Saved Map
    │
    ▼
Nav2
    │
    ▼
Localization
    │
    ▼
Navigation Planning
    │
    ▼
Controller
    │
    ▼
Four-Wheel Robot
```

---

# 🔧 Technologies Used

| Technology        | Purpose                            |
| ----------------- | ---------------------------------- |
| **ROS 2**         | Robot middleware and communication |
| **Gazebo**        | Robot simulation                   |
| **SLAM Toolbox**  | Environment mapping                |
| **Nav2**          | Autonomous navigation              |
| **RViz2**         | Visualization                      |
| **ROS 2 Control** | Robot control                      |
| **LiDAR**         | Environment sensing                |
| **URDF/Xacro**    | Robot modeling                     |
| **Python**        | ROS 2 launch files                 |
| **YAML**          | Configuration files                |
| **SDF**           | Gazebo world                       |

---

# 📦 ROS 2 Package

The repository contains the following ROS 2 package:

```text
four_wheel
```

The package contains the robot description, simulation environment, SLAM configuration, Nav2 configuration, controllers, launch files, and RViz configurations.

---

# 📁 Project Structure

The existing `four_wheel` package structure is preserved.

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

# 🤖 Robot Description

The robot model is created using URDF/Xacro.

The robot description contains:

```text
urdf/
├── inertial_macros.xacro
├── lidar.xacro
├── robot_core.xacro
├── robot.urdf.xacro
└── ros2_control.xacro
```

### Main components

**`robot.urdf.xacro`**

Main robot description.

**`robot_core.xacro`**

Core robot structure.

**`ros2_control.xacro`**

ROS 2 Control integration.

**`lidar.xacro`**

LiDAR sensor description.

**`inertial_macros.xacro`**

Reusable inertial properties/macros.

---

# 📡 LiDAR

The robot includes a LiDAR sensor for environment perception.

The LiDAR configuration is contained in:

```text
urdf/lidar.xacro
```

The LiDAR provides the range measurements required by the SLAM system to understand the surrounding environment.

---

# 🌍 Gazebo Simulation

The robot is simulated using Gazebo.

The simulation environment is defined in:

```text
worlds/
└── empty_world.sdf
```

The Gazebo launch file is:

```text
launch/gazebo.launch.py
```

---

# 🗺️ SLAM Mapping

The project uses SLAM to create an occupancy map of the environment.

The SLAM configuration is located in:

```text
config/mapper_params_online_async.yaml
```

The SLAM launch file is:

```text
launch/slam.launch.py
```

During mapping, the robot can be manually driven around the environment while the LiDAR observes surrounding obstacles.

The resulting map can then be saved for navigation.

---

# 🖥️ RViz Visualization

RViz2 can be used to visualize the robot and generated map.

Available RViz configurations:

```text
rviz/
├── nav.rviz
└── rviz_config.rviz
```

For SLAM visualization, set:

```text
Fixed Frame → map
```

Then add the map display using:

```text
Add → By topic → /map
```

If RViz reports:

```text
No map received
```

the Map display QoS settings may need:

```text
Reliability  = Reliable
Durability   = Transient Local
```

These settings are part of the project's current mapping workflow.

---

# 🎮 Robot Teleoperation

During mapping, the robot can be operated using:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -p stamped:=true -p frame_id:=base_link -r cmd_vel:=/diff_drive_controller/cmd_vel
```

This allows the robot to be manually driven through the environment while SLAM builds the map.

---

# 🗺️ Saved Map

The repository includes a previously generated map:

```text
worlds/maps/
├── my_map.pgm
└── my_map.yaml
```

The map can also be generated and saved using:

```bash
ros2 run nav2_map_server map_saver_cli -f ~/ros2_ws/maps/my_map
```

This produces the map files required for subsequent navigation.

---

# 🧭 Nav2 Navigation

Nav2 is used for autonomous navigation using the generated map.

The Nav2 configuration is located in:

```text
config/nav2_params.yaml
```

The navigation launch file is:

```text
launch/navigation.launch.py
```

The navigation system can use the saved map to plan and execute robot movement through the environment.

---

# 🚀 Installation

## Prerequisites

Install and configure:

* ROS 2
* Gazebo
* RViz2
* SLAM Toolbox
* Nav2
* ROS 2 Control
* `teleop_twist_keyboard`

---

## Clone the Repository

Create the workspace:

```bash
mkdir -p ~/ros2_ws/src
```

Navigate to the source directory:

```bash
cd ~/ros2_ws/src
```

Clone the repository:

```bash
git clone https://github.com/Rajvardhan16/ros2-SLAM-Nav2-robot.git
```

---

# 🔨 Build the Package

Navigate to the workspace:

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

The build and source sequence follows the project's current setup.

---

# ▶️ Execution

The complete system is operated in multiple terminals.

The recommended workflow is:

```text
Terminal 1 → Gazebo
Terminal 2 → SLAM
Terminal 3 → RViz
Terminal 4 → Teleoperation
```

After mapping:

```text
Save Map → Start Nav2
```

---

# 🟢 STEP 1 — Start Gazebo

Open **Terminal 1**:

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

# 🗺️ STEP 2 — Start SLAM

Open **Terminal 2**:

```bash
cd ~/ros2_ws
```

Source the workspace:

```bash
source install/setup.bash
```

Start SLAM:

```bash
ros2 launch four_wheel slam.launch.py
```

Keep this terminal running.

---

# 🖥️ STEP 3 — Start RViz

If RViz is needed, open another terminal:

```bash
source ~/ros2_ws/install/setup.bash
```

Then:

```bash
rviz2
```

In RViz:

```text
Fixed Frame → map
```

Add the map:

```text
Add → By topic → /map
```

If the map is not received, configure the Map display QoS as:

```text
Reliability  → Reliable
Durability   → Transient Local
```

---

# 🎮 STEP 4 — Operate the Robot

Open another terminal:

```bash
source ~/ros2_ws/install/setup.bash
```

Run:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -p stamped:=true -p frame_id:=base_link -r cmd_vel:=/diff_drive_controller/cmd_vel
```

Use the keyboard to drive the robot around the environment.

Move the robot through different areas so that the LiDAR can observe the environment and SLAM can construct the map.

---

# 💾 STEP 5 — Save the Map

Once the environment has been mapped, save the map:

```bash
ros2 run nav2_map_server map_saver_cli -f ~/ros2_ws/maps/my_map
```

The generated map consists of the required map files for later navigation.

The repository currently contains:

```text
worlds/maps/
├── my_map.pgm
└── my_map.yaml
```

---

# 🧭 STEP 6 — Start Nav2

After the map has been created and saved, start the navigation system.

Open a terminal:

```bash
cd ~/ros2_ws
```

Source the workspace:

```bash
source install/setup.bash
```

Launch Nav2:

```bash
ros2 launch four_wheel navigation.launch.py
```

This starts the robot navigation system using the configured Nav2 parameters.

---

# 🔄 Complete Mapping Workflow

```text
┌─────────────────────┐
│  Build ROS 2        │
│  four_wheel package  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Start Gazebo       │
│  gazebo.launch.py   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Start SLAM         │
│  slam.launch.py     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      RViz2          │
│  Visualize /map     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    Teleoperation    │
│   Drive the Robot   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Generate Map      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      Save Map       │
│ my_map.pgm/.yaml    │
└─────────────────────┘
```

---

# 🧭 Complete Navigation Workflow

```text
             Saved Map
                 │
                 ▼
       ┌─────────────────┐
       │      Nav2       │
       │ Navigation Stack│
       └────────┬────────┘
                │
                ▼
       ┌─────────────────┐
       │ Localization &  │
       │ Path Planning   │
       └────────┬────────┘
                │
                ▼
       ┌─────────────────┐
       │   Controllers   │
       └────────┬────────┘
                │
                ▼
       ┌─────────────────┐
       │ Four-Wheel Robot│
       └─────────────────┘
```

---

# ⚙️ Configuration Files

### Controller Configuration

```text
config/my_controllers.yaml
```

Contains controller configuration for the mobile robot.

### SLAM Configuration

```text
config/mapper_params_online_async.yaml
```

Contains SLAM configuration parameters.

### Nav2 Configuration

```text
config/nav2_params.yaml
```

Contains navigation stack configuration.

---

# 🚀 Launch Files

The package provides the following launch files:

| Launch File            | Purpose                                         |
| ---------------------- | ----------------------------------------------- |
| `gazebo.launch.py`     | Start Gazebo simulation                         |
| `slam.launch.py`       | Start SLAM                                      |
| `navigation.launch.py` | Start Nav2                                      |
| `rsp.launch.py`        | Start robot state publisher / robot description |

---

# 🖥️ RViz Configurations

Two RViz configurations are included:

```text
rviz/
├── nav.rviz
└── rviz_config.rviz
```

These configurations can be used for visualization during mapping and navigation.

---

# 🧪 Testing

The project can be tested progressively.

### Test 1 — Robot Simulation

Verify that the robot loads correctly in Gazebo.

### Test 2 — LiDAR

Verify that the LiDAR detects the surrounding environment.

### Test 3 — SLAM

Drive the robot around the environment and verify that `/map` is generated.

### Test 4 — Map Saving

Save the generated map using:

```bash
ros2 run nav2_map_server map_saver_cli -f ~/ros2_ws/maps/my_map
```

### Test 5 — Navigation

Launch Nav2 and verify autonomous navigation using the saved map.

---

# 🛠️ Development

After modifying the package, rebuild it using:

```bash
cd ~/ros2_ws
colcon build --packages-select four_wheel
```

Then source the workspace:

```bash
source install/setup.bash
```

---

# 📚 Learning Outcomes

This project provides practical experience with:

* ROS 2
* Mobile robotics
* Differential-drive control
* Four-wheel robot modeling
* URDF/Xacro
* Gazebo
* LiDAR
* SLAM
* Mapping
* RViz2
* ROS 2 Control
* Nav2
* Autonomous navigation
* Path planning
* Robot localization
* Teleoperation
* Map generation and storage

---

# 🔮 Future Improvements

Possible improvements include:

* Autonomous exploration
* Improved localization
* Multiple LiDAR sensors
* Depth camera integration
* Obstacle avoidance improvements
* Dynamic obstacle handling
* Waypoint navigation
* Autonomous map exploration
* Improved robot controller tuning
* Real hardware implementation
* Hardware-in-the-loop testing
* Integration with additional sensors

---

# 📸 Demo

Screenshots and videos can be added here.

Recommended demonstrations:

1. Four-wheel robot in Gazebo
2. LiDAR scan visualization
3. SLAM-generated map
4. RViz mapping view
5. Saved occupancy map
6. Nav2 navigation
7. Autonomous robot movement

---


# 👨‍💻 Author

**Rajvardhan**

Robotics & Automation Engineering

GitHub: **Rajvardhan16**

---

# ⭐ Repository

If you find this project useful for learning ROS 2, SLAM, Nav2, or mobile robotics, consider giving the repository a ⭐.

**Repository:** `ros2-SLAM-Nav2-robot`

---

## 📄 License

License information will be added as the project develops.
