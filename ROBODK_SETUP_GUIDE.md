# RoboDK Station Setup Guide

**Team PR2-1-1**

This guide explains how to set up your RoboDK station to work with the robot programs in this repository.

## Prerequisites

1. Install RoboDK from https://robodk.com/
2. Ensure Python 3.x is installed
3. Verify RoboDK API is available (should be included with RoboDK)

## Station Setup

### Step 1: Create a New RoboDK Station

1. Open RoboDK
2. Click **File → New Station** (or use an existing station)
3. Save the station as `Team_PR2_Station.rdk` (or your preferred name)

### Step 2: Add UR10 Robot (for Sergio)

1. Click **Library** (or press `Ctrl+L`)
2. Navigate to: **ABB / Universal Robots**
3. Drag **UR10** into your station
4. Right-click the robot → **Rename** → Name it **"UR10"** (exactly as shown)
5. Position the robot base as desired

### Step 3: Add UR5 Robot (for Diego)

1. Click **Library** (or press `Ctrl+L`)
2. Navigate to: **ABB / Universal Robots**
3. Drag **UR5** into your station
4. Right-click the robot → **Rename** → Name it **"UR5"** (exactly as shown)
5. Position the robot base away from UR10 to avoid collision

### Step 4: Create Targets for UR10

Create the following targets for UR10:

1. **UR10_PickTarget**:
   - Right-click on UR10 → **Add Target**
   - Rename to: `UR10_PickTarget`
   - Position the target where objects should be picked
   - Make sure UR10 can reach this position

2. **UR10_PlaceTarget**:
   - Right-click on UR10 → **Add Target**
   - Rename to: `UR10_PlaceTarget`
   - Position the target where objects should be placed
   - Make sure UR10 can reach this position

### Step 5: Create Targets for UR5

Create the following targets for UR5:

1. **UR5_Fold1_Bottom**:
   - Right-click on UR5 → **Add Target**
   - Rename to: `UR5_Fold1_Bottom`
   - Position for folding bottom flap

2. **UR5_Fold2_Left**:
   - Right-click on UR5 → **Add Target**
   - Rename to: `UR5_Fold2_Left`
   - Position for folding left side

3. **UR5_Fold3_Right**:
   - Right-click on UR5 → **Add Target**
   - Rename to: `UR5_Fold3_Right`
   - Position for folding right side

4. **UR5_Fold4_Top**:
   - Right-click on UR5 → **Add Target**
   - Rename to: `UR5_Fold4_Top`
   - Position for folding top flap

5. **UR5_ConveyorTarget**:
   - Right-click on UR5 → **Add Target**
   - Rename to: `UR5_ConveyorTarget`
   - Position where box should be placed on conveyor

### Step 6: Add Optional Objects (Recommended)

Add visual objects to make the station more realistic:

1. **Pick Object** (for UR10):
   - Click **Library** → Search for "cube" or "box"
   - Drag an object near UR10_PickTarget
   - This helps visualize what UR10 is picking

2. **Conveyor Belt** (for UR5):
   - Click **Library** → Search for "conveyor"
   - Add a conveyor near UR5_ConveyorTarget
   - Position it appropriately

3. **Box to Fold** (for UR5):
   - Add a flat box object near the folding positions
   - This helps visualize the folding operation

## Verifying Your Setup

### Check Robot Names
1. In the **Station Tree**, verify:
   - UR10 robot is named exactly "UR10"
   - UR5 robot is named exactly "UR5"

### Check Target Names
2. Expand each robot in the Station Tree and verify all targets exist:
   - For UR10: `UR10_PickTarget`, `UR10_PlaceTarget`
   - For UR5: `UR5_Fold1_Bottom`, `UR5_Fold2_Left`, `UR5_Fold3_Right`, `UR5_Fold4_Top`, `UR5_ConveyorTarget`

### Test Reachability
3. For each target:
   - Double-click the target to move the robot
   - Verify the robot can reach the position without collision
   - Adjust target positions if needed

## Loading and Running Programs

### Option 1: Run from RoboDK Interface

**For UR10:**
1. Right-click on UR10 robot
2. Select **Add Program → Python**
3. Browse and select `UR10_PickAndPlace/ur10_program.py`
4. Double-click the program to run it

**For UR5:**
1. Right-click on UR5 robot
2. Select **Add Program → Python**
3. Browse and select `UR5_BoxFolding/ur5_program.py`
4. Double-click the program to run it

### Option 2: Run from Command Line

Make sure RoboDK is running with your station loaded, then:

```bash
# Terminal 1: Run UR10 program
cd /path/to/RoboDK-project-Team-PR2-1-1
python UR10_PickAndPlace/ur10_program.py

# Terminal 2: Run UR5 program (in another terminal)
cd /path/to/RoboDK-project-Team-PR2-1-1
python UR5_BoxFolding/ur5_program.py
```

## Customization

### Adjusting Joint Positions

Edit the configuration files to match your station:

**UR10_PickAndPlace/ur10_config.py:**
```python
HOME_JOINTS = [0, -90, -90, -90, 90, 0]  # Adjust these values
```

**UR5_BoxFolding/ur5_config.py:**
```python
HOME_JOINTS = [0, -90, -90, -90, 90, 0]  # Adjust these values
```

### Changing Target Names

If you use different target names, update the configuration files:

**In ur10_config.py:**
```python
PICK_TARGET = "YourPickTargetName"
PLACE_TARGET = "YourPlaceTargetName"
```

**In ur5_config.py:**
```python
FOLDING_TARGET_1 = "YourFoldTarget1"
# ... etc
```

## Troubleshooting

### "Robot not found" Error
- Verify robot names are exactly "UR10" and "UR5" (case-sensitive)
- Make sure RoboDK is running with the station loaded

### "Target not found" Warning
- Check target names match configuration files exactly
- Verify targets are attached to the correct robot in Station Tree

### Robot Doesn't Move
- Check if robot is in simulation mode (not real robot connection)
- Verify targets are reachable (no joint limits exceeded)
- Check for collisions in the station

### Handshake Timeout
- Make sure both robot programs can communicate
- Check that handshake module is accessible from both programs
- Verify both programs are running simultaneously for synchronized operation

## Next Steps

Once your station is set up:

1. **Sergio**: Test UR10 program and adjust as needed
2. **Diego**: Test UR5 program and adjust as needed
3. **Felix**: Review handshake communication between robots
4. **All**: Document improvements in `/Documentation/IMPROVEMENTS.md`

## Tips

- Save your RoboDK station frequently
- Use **Ctrl+S** to save station
- Use **Ctrl+Z** to undo changes
- Test each robot individually before running both simultaneously
- Start with slow speeds and increase after verifying movements

## Additional Resources

- RoboDK Documentation: https://robodk.com/doc/en/
- RoboDK API Documentation: https://robodk.com/doc/en/PythonAPI/
- Universal Robots Documentation: https://www.universal-robots.com/

---

**For questions about this setup, contact your team members according to their responsibilities.**
