# UR10 Pick and Place Program

**Responsible:** Sergio

## Purpose
This folder contains the RoboDK program for the UR10 robot to perform pick and place operations.

## Description
The UR10 robot is programmed to:
- Pick objects from a designated target in the RoboDK station
- Place objects at target positions in the RoboDK station
- Coordinate with the UR5 robot through handshake signals

## Files
- `ur10_program.py` - Main RoboDK program for UR10 pick and place operations
- `ur10_config.py` - Configuration parameters for UR10

## RoboDK Setup Required

### In your RoboDK station, you need:
1. **Robot:** A UR10 robot named "UR10"
2. **Targets:**
   - `UR10_PickTarget` - Location where objects are picked
   - `UR10_PlaceTarget` - Location where objects are placed
3. **Reference Frame:** "UR10 Base" (optional, for reference)

### Running the Program
1. Open your RoboDK station with the UR10 robot
2. Create the required targets (UR10_PickTarget, UR10_PlaceTarget)
3. Right-click on the UR10 robot → Add Program → Python
4. Load `ur10_program.py` into the Python program
5. Run the program from RoboDK

Alternatively, you can run the script directly:
```bash
python ur10_program.py
```
(Note: RoboDK must be running with the station loaded)

## Integration
This program uses the handshake module in the `/Handshake` folder to communicate with the UR5 robot and ensure synchronized operations.

## Instructions for Sergio
1. Set up your RoboDK station with UR10 robot and targets
2. Adjust joint angles in `ur10_config.py` as needed
3. Customize target names if different from defaults
4. Implement actual gripper control (marked with TODO)
5. Test the program in RoboDK simulation
6. Document any improvements in `/Documentation/IMPROVEMENTS.md`

## Configuration
Edit `ur10_config.py` to customize:
- `HOME_JOINTS` - Home position joint angles
- `PICK_TARGET` - Name of pick target in RoboDK station
- `PLACE_TARGET` - Name of place target in RoboDK station
- `SAFE_HEIGHT` - Safety height for approach movements
- Speed and gripper settings
