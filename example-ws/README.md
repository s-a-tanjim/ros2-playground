# Commands
```sh
# Create package
cd workspace/src
# In python
ros2 pkg create --build-type ament_python talker_listener
# In Cpp
ros2 pkg create --build-type ament_cmake custom_interface
# Create package with dependencies
ros2 pkg create --build-type ament_python example_service --dependencies rclpy custom_interfaces


# Install dependencies
cd workspace
rosdep install -i --from-path src --rosdistro foxy -y

# Build package
colcon build

# Run package
source ./install/setup.zsh
ros2 run <package_name> <nodeName>    # ie: ros2 run talker_listener talkerNode

# Using launch file
ros2 launch <package-name> <launch-file-name>.py # ie: ros2 launch talker_listener talker_listener.launch.py
```

# Helper commands
```sh
ros2 node list

ros2 topic list

ros2 topic echo /topic_name

ros2 interface show <InterfaceName> # ie: ros2 interface show custom_interface/srv/AddTwoInts

```