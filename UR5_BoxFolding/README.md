# UR5 Box Folding and Conveyor Program - TEMPLATE

**Responsible:** Diego

## Purpose
This folder contains a **template** for the UR5 robot box folding and conveyor operations in RoboDK.
Diego should build upon this template to implement the complete logic for the project.

## Description
The UR5 robot template includes:
- Connection to RoboDK and robot setup
- 4-step box folding sequence
- Conveyor placement function
- Gripper control placeholders
- Handshake coordination with UR10
- Main program loop structure

## Files
- `ur5_program.py` - **TEMPLATE** RoboDK program for UR5 box folding
- `README.md` - This file

## RoboDK Station Setup Required

### In your RoboDK station, you need:
1. **Robot:** A UR5 robot named **"UR5"**
2. **Targets:** (Create these targets in your station)
   - `UR5_Home` - Home/starting position
   - `UR5_Fold1` - Position for folding bottom flap
   - `UR5_Fold2` - Position for folding left side
   - `UR5_Fold3` - Position for folding right side
   - `UR5_Fold4` - Position for folding top flap and seal
   - `UR5_ConveyorPlace` - Position to place box on conveyor
3. **Optional:** Gripper tool attached to robot
4. **Optional:** Conveyor belt and box objects

### How to Create Targets:
1. Move the robot to desired position manually in RoboDK
2. Right-click on robot → **Add Target** → **New Target**
3. Rename the target according to the list above
4. Repeat for all targets

## Running the Program

### From RoboDK Interface:
1. Open your RoboDK station with UR5 robot and targets
2. Right-click on UR5 robot → **Add Program** → **Python**
3. Load `ur5_program.py`
4. Double-click the program to run

### From Command Line:
```bash
python ur5_program.py
```
(Note: RoboDK must be running with the station loaded)

## Template Structure

The template provides:

### Connection Setup
```python
RDK = robolink.Robolink()
robot = RDK.Item('UR5', robolink.ITEM_TYPE_ROBOT)
```

### Helper Functions
- `move_with_offset_z()` - Move with Z offset
- `open_gripper()` - Gripper opening (placeholder)
- `close_gripper()` - Gripper closing (placeholder)
- `fold_box()` - 4-step folding sequence
- `place_on_conveyor()` - Conveyor placement

### Main Program
- Initialization and home position
- Main loop with cycle counter
- Handshake coordination with UR10
- Error handling

## Instructions for Diego

1. **Setup your RoboDK station:**
   - Add UR5 robot named "UR5"
   - Create all required targets listed above
   - Add conveyor belt (optional)
   - Add box objects to fold (optional)

2. **Customize the template:**
   - Implement actual gripper control in `open_gripper()` and `close_gripper()`
   - Modify the folding logic as needed for your box design
   - Add actual folding tool actions in `fold_box()`
   - Adjust configuration parameters (speeds, heights, cycles, timing)

3. **Test your implementation:**
   - Test each folding step individually
   - Run the complete program
   - Verify coordination with UR10

4. **Document changes:**
   - Document any modifications in `/Documentation/IMPROVEMENTS.md`
   - Update this README if you change the structure significantly

## Configuration

At the top of `ur5_program.py`, you can adjust:

```python
SAFE_HEIGHT_OFFSET = 100.0  # mm above folding/conveyor positions
FOLD_PAUSE_TIME = 0.5       # seconds to pause at each folding position
CONVEYOR_WAIT_TIME = 2.0    # seconds to wait after placing on conveyor
MAX_CYCLES = 10             # Number of box folding cycles
SPEED_FACTOR = 1.0          # Speed multiplier (0.1 to 1.0)
```

## Folding Sequence

The template implements a 4-step folding sequence:
1. **Fold bottom flap** (UR5_Fold1)
2. **Fold left side** (UR5_Fold2)
3. **Fold right side** (UR5_Fold3)
4. **Fold top flap and seal** (UR5_Fold4)

Each step moves to the target, pauses briefly, then continues to the next step.

## Handshake Coordination

The template uses handshake signals to coordinate with UR10:
- Waits for UR10's `COMPLETE` before starting folding
- Sends `READY` after folding is complete
- This ensures proper synchronization between robots

## Example Workflow

1. UR5 waits for UR10 COMPLETE signal
2. UR5 folds box (4 steps)
3. UR5 signals READY
4. UR5 places box on conveyor
5. Repeat

## Troubleshooting

**Robot not found:**
- Make sure robot is named exactly "UR5" in your station

**Targets not found:**
- Create all required targets in your station
- Check target names match exactly (case-sensitive)

**Program doesn't move robot:**
- Check if targets are reachable
- Verify no collisions in station
- Check robot is not in error state

## Need Help?

- Check `/Documentation/TEAM_RESPONSIBILITIES.md` for team contacts
- See `/ROBODK_SETUP_GUIDE.md` for detailed station setup
- Review the example files provided by the instructor
