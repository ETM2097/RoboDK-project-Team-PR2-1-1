# Handshake Communication Module

**Responsible for Review:** Felix

## Purpose
This folder contains the handshake communication system that enables the UR10 and UR5 robots to coordinate and work simultaneously.

## Parameters
The protocol.py provides:
- `sensor1`: Represents the state of the sensor at the beginning of the first conveyor belt, where the UR5e places the box.
- `sensor2`: Represents the state of the sensor at the end of the first conveyor belt, where the UR5e places the box.
- `sensor3`: Represents the state of the sensor at the beginning of the second conveyor belt, where the UR10e places the objects into the box.
- `sensor4`: Represents the state of the sensor at the end of the bottles conveyor belt.
- `sensor5`: Represents the state of the sensor at the end of the second conveyor belt.

## Integration

### UR5.py
When moving the belt, you need to check two sensors: `sensor2` and `sensor3`. If both sensors are ON, the conveyor belt cannot move at this moment. If `sensor2` is ON, you cannot move the conveyor belt. If `sensor1` is ON, the robot cannot move at this moment.

When moving the box from the first conveyor belt to the second one, you need to set `sensor2` to OFF.

### UR10.py
When placing the objects into the box, you need to check `sensor3`. If this sensor is ON, you can move the robot, but the conveyor belt cannot move. When the robot finishes the current task, you need to set `sensor4` to OFF and move the conveyor belt.

If `sensor5` is ON, you cannot move the belt until you move the box from the second conveyor belt to the third one.



