# UR10 Pick and Place Program

**Responsible:** Sergio

## Purpose
This folder contains the robot program for the UR10 robot to perform pick and place operations.

## Description
The UR10 robot is programmed to:
- Pick objects from a designated location
- Place objects at target positions
- Coordinate with the UR5 robot through handshake signals

## Files
- `ur10_program.py` - Main program for UR10 pick and place operations
- `ur10_config.py` - Configuration parameters for UR10

## Integration
This program uses the handshake module in the `/Handshake` folder to communicate with the UR5 robot and ensure synchronized operations.

## Instructions for Sergio
1. Implement the pick and place logic in `ur10_program.py`
2. Configure robot parameters in `ur10_config.py`
3. Use the handshake functions to coordinate with UR5
4. Test the program and document any improvements in `/Documentation`
