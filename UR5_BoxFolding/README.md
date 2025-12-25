# UR5 Box Folding and Conveyor Program - TEMPLATE (You MUST create your own README)
This is a templated created by Copilot, you should create your own README in order to fully comprehend your code. Visit [This Part](README.md#instructions-for-diego) for knowing your work.

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
   - Create all required targets for correctly folding and placing the box
   - Add conveyor belt targets and frame correctly

2. **Program the functionalities:**
   - Implement actual griper functions, for setting and unsetting the tool (simulated)
   - Program the robot movement and object tracking needed for the correct functionality
   - Add logic for corretcly change visuals mid-action
   - Adjust configuration parameters (speeds, heights, cycles, timing) acording to the tasks
   - Set correctly the semaphores needed for the rest of the station.

3. **Test your implementation:**
   - Test each folding step individually
   - Run the complete program
   - Verify coordination with UR10

4. **Document changes:**
   - Document any modifications in `/Documentation/IMPROVEMENTS.md`
   - Update this README if you change the structure significantly

## Example Workflow

1. UR5 waits for boxes being aviable or there is place on the conveyor
2. UR5 folds box
3. UR5 places the box in the conveyor setting READY for the conveyor to move (can be just a continuously moving conveyor for simpler logic)
4. UR5 signals READY when the box gets to place frame
5. (Optional) Extrapolate the UR5-UR10 communication with it's own python program for box tracking ASK FELIX
7. Repeat

## Troubleshooting

Here you will post regular or recurring problems with your code

## Need Help?

- Check `/Documentation/TEAM_RESPONSIBILITIES.md` for team contacts
- See `/ROBODK_SETUP_GUIDE.md` for detailed station setup
- Review the example files provided by the instructor
