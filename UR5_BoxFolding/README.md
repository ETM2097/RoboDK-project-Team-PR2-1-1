# UR5 Box Folding and Conveyor Program

**Responsible:** Diego

## Purpose
This folder contains the RoboDK program for the UR5 robot to fold boxes and place them on the conveyor.

## Description
The UR5 robot is programmed to:
- Fold boxes according to a 4-step sequence using targets in the RoboDK station
- Place folded boxes on the conveyor belt
- Coordinate with the UR10 robot through handshake signals

## Files
- `ur5_program.py` - Main RoboDK program for UR5 box folding and conveyor operations
- `ur5_config.py` - Configuration parameters for UR5

## RoboDK Setup Required

### In your RoboDK station, you need:
1. **Robot:** A UR5 robot named "UR5"
2. **Targets:**
   - `UR5_Fold1_Bottom` - Position for folding bottom flap
   - `UR5_Fold2_Left` - Position for folding left side
   - `UR5_Fold3_Right` - Position for folding right side
   - `UR5_Fold4_Top` - Position for folding top flap and seal
   - `UR5_ConveyorTarget` - Location on conveyor belt
3. **Reference Frame:** "UR5 Base" (optional, for reference)

### Running the Program
1. Open your RoboDK station with the UR5 robot
2. Create the required targets (folding positions and conveyor target)
3. Right-click on the UR5 robot → Add Program → Python
4. Load `ur5_program.py` into the Python program
5. Run the program from RoboDK

Alternatively, you can run the script directly:
```bash
python ur5_program.py
```
(Note: RoboDK must be running with the station loaded)

## Integration
This program uses the handshake module in the `/Handshake` folder to communicate with the UR10 robot and ensure synchronized operations.

## Instructions for Diego
1. Set up your RoboDK station with UR5 robot and all folding targets
2. Adjust joint angles in `ur5_config.py` as needed
3. Customize target names if different from defaults
4. Implement actual gripper control (marked with TODO)
5. Test the folding sequence in RoboDK simulation
6. Document any improvements in `/Documentation/IMPROVEMENTS.md`

## Configuration
Edit `ur5_config.py` to customize:
- `HOME_JOINTS` - Home position joint angles
- `FOLDING_TARGET_*` - Names of folding targets in RoboDK station
- `CONVEYOR_TARGET` - Name of conveyor target in RoboDK station
- `SAFE_HEIGHT` - Safety height for approach movements
- `CONVEYOR_WAIT_TIME` - Time to wait after placing box
- Speed and gripper settings
