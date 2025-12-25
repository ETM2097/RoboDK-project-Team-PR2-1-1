# UR10 Pick and Place Program - TEMPLATE (You MUST create your own README)

**Responsible:** Sergio

## Purpose
This folder contains a **template** for the UR10 robot pick and place operations in RoboDK.
Sergio should build upon this template to implement the complete logic for the project.

## Description
The UR10 robot template includes:
- Connection to RoboDK and robot setup
- Basic pick and place functions
- Gripper control placeholders
- Handshake coordination with UR5
- Main program loop structure

## Files
- `ur10_program.py` - **TEMPLATE** RoboDK program for UR10 pick and place
- `README.md` - This file

## RoboDK Station Setup Required

### In your RoboDK station, you need:
1. **Robot:** A UR10 robot named **"UR10"**
2. **Targets:** (Create these targets in your station)
   - `UR10_Home` - Home/starting position
   - `UR10_PrePick` - Pre-pick approach position (above pick location)
   - `UR10_Pick` - Pick position
   - `UR10_PrePlace` - Pre-place approach position (above place location)
   - `UR10_Place` - Place position
3. **Optional:** Gripper tool attached to robot
4. **Optional:** Objects to pick/place

### How to Create Targets:
1. Move the robot to desired position manually in RoboDK
2. Right-click on robot → **Add Target** → **New Target**
3. Rename the target according to the list above
4. Repeat for all targets

## Running the Program

### From RoboDK Interface:
1. Open your RoboDK station with UR10 robot and targets
2. Right-click on UR10 robot → **Add Program** → **Python**
3. Load `ur10_program.py`
4. Double-click the program to run

### From Command Line:
```bash
python ur10_program.py
```
(Note: RoboDK must be running with the station loaded)

## Template Structure

The template provides:

### Connection Setup
```python
RDK = robolink.Robolink()
robot = RDK.Item('UR10', robolink.ITEM_TYPE_ROBOT)
```

### Helper Functions
- `move_with_offset_z()` - Move with Z offset
- `open_gripper()` - Gripper opening (placeholder)
- `close_gripper()` - Gripper closing (placeholder)
- `pick_object()` - Basic pick operation
- `place_object()` - Basic place operation

### Main Program
- Initialization and home position
- Main loop with cycle counter
- Handshake coordination with UR5
- Error handling

## Instructions for Sergio

1. **Setup your RoboDK station:**
   - Add UR10 robot named "UR10"
   - Create all required targets listed above
   - Add any objects you need to pick/place

2. **Customize the template:**
   - Implement actual gripper control in `open_gripper()` and `close_gripper()`
   - Modify the pick and place logic as needed
   - Add additional helper functions if needed
   - Adjust configuration parameters (speeds, heights, cycles)

3. **Test your implementation:**
   - Test each function individually
   - Run the complete program
   - Verify coordination with UR5

4. **Document changes:**
   - Document any modifications in `/Documentation/IMPROVEMENTS.md`
   - Update this README if you change the structure significantly

## Configuration

At the top of `ur10_program.py`, you can adjust:

```python
SAFE_HEIGHT_OFFSET = 100.0  # mm above pick/place positions
MAX_CYCLES = 10             # Number of pick and place cycles
SPEED_FACTOR = 1.0          # Speed multiplier (0.1 to 1.0)
```

## Handshake Coordination

The template uses handshake signals to coordinate with UR5:
- Sends `READY` when starting a cycle
- Sends `COMPLETE` after finishing pick/place
- Waits for UR5's `READY` before next cycle

## Example Workflow

1. UR10 signals READY
2. UR10 picks object
3. UR10 places object
4. UR10 signals COMPLETE
5. UR10 waits for UR5 READY
6. Repeat

## Troubleshooting

**Robot not found:**
- Make sure robot is named exactly "UR10" in your station

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
