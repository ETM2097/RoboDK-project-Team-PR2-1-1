"""
UR10 Pick and Place Program - TEMPLATE
Responsible: Sergio

This is a template for the UR10 robot pick and place operations in RoboDK.
Sergio should build upon this template to implement the complete logic.

SETUP REQUIRED IN ROBODK STATION:
1. A UR10 robot named 'UR10'
2. Targets: 'UR10_Home', 'UR10_PrePick', 'UR10_Pick', 'UR10_PrePlace', 'UR10_Place'
3. (Optional) A gripper tool attached to the robot
4. Objects to pick (can be added as needed)

This script coordinates with the UR5 program using handshake signals.
"""

from robodk import robolink, robomath
import sys
import os
import time

# Add parent directory to path to import handshake module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Handshake.handshake import RobotHandshake

# ============================================================================
# SETUP - Connect to RoboDK and get robot/targets
# ============================================================================

RDK = robolink.Robolink()
robot = RDK.Item('UR10', robolink.ITEM_TYPE_ROBOT)

if not robot.Valid():
    raise Exception("UR10 robot not found in RoboDK station. Please add a UR10 robot named 'UR10'.")

print(f"[UR10] Connected to robot: {robot.Name()}")

# Get targets - Sergio: Add these targets to your RoboDK station
t_home = RDK.Item('UR10_Home')
t_prepick = RDK.Item('UR10_PrePick')
t_pick = RDK.Item('UR10_Pick')
t_preplace = RDK.Item('UR10_PrePlace')
t_place = RDK.Item('UR10_Place')

# Optional: Get gripper tool
# gripper = RDK.Item('Gripper', robolink.ITEM_TYPE_TOOL)

# Initialize handshake for coordination with UR5
handshake = RobotHandshake("UR10")

# ============================================================================
# CONFIGURATION - Adjust these parameters as needed
# ============================================================================

SAFE_HEIGHT_OFFSET = 100.0  # mm above pick/place positions
MAX_CYCLES = 10  # Number of pick and place cycles
SPEED_FACTOR = 1.0  # Speed multiplier (0.1 to 1.0)

# ============================================================================
# HELPER FUNCTIONS - Sergio: Add more functions as needed
# ============================================================================

def move_with_offset_z(target, z_offset):
    """
    Move to a target with a Z offset
    
    Args:
        target: RoboDK target item
        z_offset: Z offset in mm
    """
    if target.Valid():
        pose = target.Pose()
        robot.MoveL(pose * robomath.transl(0, 0, z_offset))
    else:
        print(f"[UR10] Warning: Target not found")

def open_gripper():
    """
    Open the gripper
    Sergio: Implement actual gripper control here
    """
    print("[UR10] Opening gripper...")
    # TODO: Add gripper opening code
    # Example: RDK.setParam('GripperOpen', 1)
    time.sleep(0.5)

def close_gripper():
    """
    Close the gripper
    Sergio: Implement actual gripper control here
    """
    print("[UR10] Closing gripper...")
    # TODO: Add gripper closing code
    # Example: RDK.setParam('GripperClose', 1)
    time.sleep(0.5)

def pick_object(object_name=None):
    """
    Pick an object at the pick location
    
    Args:
        object_name: Optional name of object to pick from station
    """
    print("[UR10] Executing pick operation...")
    
    # Move to pre-pick position
    if t_prepick.Valid():
        robot.MoveJ(t_prepick)
    
    # Move to pick position
    if t_pick.Valid():
        robot.MoveL(t_pick)
    
    # Close gripper
    close_gripper()
    
    # Optional: Attach object to gripper
    if object_name:
        obj = RDK.Item(object_name, robolink.ITEM_TYPE_OBJECT)
        if obj.Valid():
            gripper = robot.Childs()[0] if len(robot.Childs()) > 0 else robot
            obj.setParentStatic(gripper)
    
    # Move back to pre-pick
    if t_prepick.Valid():
        robot.MoveL(t_prepick)
    
    print("[UR10] Pick complete")

def place_object(object_name=None):
    """
    Place an object at the place location
    
    Args:
        object_name: Optional name of object to place
    """
    print("[UR10] Executing place operation...")
    
    # Move to pre-place position
    if t_preplace.Valid():
        robot.MoveJ(t_preplace)
    
    # Move to place position
    if t_place.Valid():
        robot.MoveL(t_place)
    
    # Open gripper
    open_gripper()
    
    # Optional: Detach object from gripper
    if object_name:
        obj = RDK.Item(object_name, robolink.ITEM_TYPE_OBJECT)
        if obj.Valid():
            station = RDK.Item('Station')
            obj.setParentStatic(station)
    
    # Move back to pre-place
    if t_preplace.Valid():
        robot.MoveL(t_preplace)
    
    print("[UR10] Place complete")

# ============================================================================
# MAIN PROGRAM - Sergio: Implement your logic here
# ============================================================================

def main():
    """
    Main program loop
    Sergio: This is where you implement the pick and place logic
    """
    print("="*60)
    print("UR10 Pick and Place Program")
    print("Responsible: Sergio")
    print("="*60)
    
    # Move to home position
    if t_home.Valid():
        print("[UR10] Moving to home position...")
        robot.MoveJ(t_home)
    else:
        print("[UR10] Warning: Home target not found. Please add 'UR10_Home' target.")
    
    # Main loop
    cycle_count = 0
    
    while cycle_count < MAX_CYCLES:
        print(f"\n[UR10] --- Cycle {cycle_count + 1}/{MAX_CYCLES} ---")
        
        # Signal that UR10 is ready to start
        handshake.send_signal("UR10", RobotHandshake.SIGNAL_READY)
        print("[UR10] Signaled READY to UR5")
        
        # Execute pick operation
        pick_object()
        
        # Execute place operation
        place_object()
        
        # Signal that UR10 has completed its operation
        handshake.send_signal("UR10", RobotHandshake.SIGNAL_COMPLETE)
        print("[UR10] Signaled COMPLETE to UR5")
        
        # Wait for UR5 to be ready before next cycle
        print("[UR10] Waiting for UR5 to be ready...")
        handshake.wait_for_signal("UR5", RobotHandshake.SIGNAL_READY)
        print("[UR10] UR5 is ready, continuing...")
        
        cycle_count += 1
        time.sleep(0.5)  # Small delay between cycles
    
    # Return to home
    if t_home.Valid():
        print("[UR10] Returning to home position...")
        robot.MoveJ(t_home)
    
    print("[UR10] Program completed successfully!")

# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[UR10] Program interrupted by user")
    except Exception as e:
        print(f"[UR10] Error: {e}")
        import traceback
        traceback.print_exc()

