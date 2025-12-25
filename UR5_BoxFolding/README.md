# UR5 Box Folding and Conveyor Program

**Responsible:** Diego

## Purpose
This folder contains the robot program for the UR5 robot to fold boxes and place them on the conveyor.

## Description
The UR5 robot is programmed to:
- Fold boxes according to the specified pattern
- Place folded boxes on the conveyor belt
- Coordinate with the UR10 robot through handshake signals

## Files
- `ur5_program.py` - Main program for UR5 box folding and conveyor operations
- `ur5_config.py` - Configuration parameters for UR5

## Integration
This program uses the handshake module in the `/Handshake` folder to communicate with the UR10 robot and ensure synchronized operations.

## Instructions for Diego
1. Implement the box folding logic in `ur5_program.py`
2. Configure robot parameters in `ur5_config.py`
3. Use the handshake functions to coordinate with UR10
4. Test the program and document any improvements in `/Documentation`
