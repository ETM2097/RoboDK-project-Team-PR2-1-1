"""
UR5 Box Folding and Conveyor Program - TEMPLATE
Responsible: Diego

This is a template for the UR5 robot box folding and conveyor operations in RoboDK.
Diego should build upon this template to implement the complete logic.

SETUP REQUIRED IN ROBODK STATION:
1. A UR5 robot named 'UR5'
2. Targets: 'UR5_Home', 'UR5_Fold1', 'UR5_Fold2', 'UR5_Fold3', 'UR5_Fold4', 'UR5_ConveyorPlace'
3. (Optional) A gripper tool attached to the robot
4. (Optional) Conveyor belt and box objects

This script coordinates with the UR10 program using handshake signals.
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
robot = RDK.Item('UR5', robolink.ITEM_TYPE_ROBOT)

if not robot.Valid():
    raise Exception("UR5 robot not found in RoboDK station. Please add a UR5 robot named 'UR5'.")

print(f"[UR5] Connected to robot: {robot.Name()}")

# Get targets - Diego: Add these targets to your RoboDK station
t_home = RDK.Item('UR5_Home')
t_fold1 = RDK.Item('UR5_Fold1')  # Fold bottom flap
t_fold2 = RDK.Item('UR5_Fold2')  # Fold left side
t_fold3 = RDK.Item('UR5_Fold3')  # Fold right side
t_fold4 = RDK.Item('UR5_Fold4')  # Fold top flap
t_conveyor = RDK.Item('UR5_ConveyorPlace')

# Optional: Get gripper tool
# gripper = RDK.Item('Gripper', robolink.ITEM_TYPE_TOOL)

# Initialize handshake for coordination with UR10
handshake = RobotHandshake("UR5")

# ============================================================================
# CONFIGURATION - Adjust these parameters as needed
# ============================================================================

SAFE_HEIGHT_OFFSET = 100.0  # mm above folding/conveyor positions
FOLD_PAUSE_TIME = 0.5  # seconds to pause at each folding position
CONVEYOR_WAIT_TIME = 2.0  # seconds to wait after placing on conveyor
MAX_CYCLES = 10  # Number of box folding cycles
SPEED_FACTOR = 1.0  # Speed multiplier (0.1 to 1.0)

# ============================================================================
# HELPER FUNCTIONS - Diego: Add more functions as needed
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
        print(f"[UR5] Warning: Target not found")

def open_gripper():
    """
    Open the gripper
    Diego: Implement actual gripper control here
    """
    print("[UR5] Opening gripper...")
    # TODO: Add gripper opening code
    # Example: RDK.setParam('GripperOpen', 1)
    time.sleep(0.3)

def close_gripper():
    """
    Close the gripper
    Diego: Implement actual gripper control here
    """
    print("[UR5] Closing gripper...")
    # TODO: Add gripper closing code
    # Example: RDK.setParam('GripperClose', 1)
    time.sleep(0.3)

def fold_box(box_id):
    """
    Execute the 4-step box folding sequence
    
    Args:
        box_id: Identifier for the box being folded
    """
    print(f"[UR5] Starting folding sequence for box {box_id}...")
    
    folding_steps = [
        (t_fold1, "Fold bottom flap"),
        (t_fold2, "Fold left side"),
        (t_fold3, "Fold right side"),
        (t_fold4, "Fold top flap and seal")
    ]
    
    for i, (target, description) in enumerate(folding_steps, 1):
        print(f"[UR5] Step {i}/4: {description}")
        
        if target.Valid():
            # Move to folding position
            robot.MoveL(target)
            
            # Pause to simulate folding action
            time.sleep(FOLD_PAUSE_TIME)
            
            # Diego: Add actual folding action here
            # Example: activate folding tool, apply pressure, etc.
        else:
            print(f"[UR5] Warning: Target not found for step {i}")
    
    print(f"[UR5] Box {box_id} folded successfully")

def place_on_conveyor(box_id, box_name=None):
    """
    Place the folded box on the conveyor belt
    
    Args:
        box_id: Identifier for the box
        box_name: Optional name of box object in station
    """
    print(f"[UR5] Placing box {box_id} on conveyor...")
    
    if t_conveyor.Valid():
        # Move to conveyor position
        robot.MoveJ(t_conveyor)
        
        # Open gripper to release box
        open_gripper()
        
        # Optional: Detach box object
        if box_name:
            box = RDK.Item(box_name, robolink.ITEM_TYPE_OBJECT)
            if box.Valid():
                station = RDK.Item('Station')
                box.setParentStatic(station)
        
        # Wait for conveyor to move box away
        print(f"[UR5] Waiting for conveyor to move box...")
        time.sleep(CONVEYOR_WAIT_TIME)
    else:
        print("[UR5] Warning: Conveyor target not found")
    
    print(f"[UR5] Box {box_id} placed on conveyor")

# ============================================================================
# MAIN PROGRAM - Diego: Implement your logic here
# ============================================================================

def main():
    """
    Main program loop
    Diego: This is where you implement the box folding and conveyor logic
    """
    print("="*60)
    print("UR5 Box Folding and Conveyor Program")
    print("Responsible: Diego")
    print("="*60)
    
    # Move to home position
    if t_home.Valid():
        print("[UR5] Moving to home position...")
        robot.MoveJ(t_home)
    else:
        print("[UR5] Warning: Home target not found. Please add 'UR5_Home' target.")
    
    # Main loop
    cycle_count = 0
    
    while cycle_count < MAX_CYCLES:
        print(f"\n[UR5] --- Cycle {cycle_count + 1}/{MAX_CYCLES} ---")
        
        # Wait for UR10 to complete its operation before starting
        print("[UR5] Waiting for UR10 to complete...")
        handshake.wait_for_signal("UR10", RobotHandshake.SIGNAL_COMPLETE)
        print("[UR5] UR10 completed, starting folding...")
        
        # Execute box folding sequence
        fold_box(cycle_count + 1)
        
        # Signal that UR5 is ready
        handshake.send_signal("UR5", RobotHandshake.SIGNAL_READY)
        print("[UR5] Signaled READY to UR10")
        
        # Place box on conveyor
        place_on_conveyor(cycle_count + 1)
        
        cycle_count += 1
        time.sleep(0.5)  # Small delay between cycles
    
    # Return to home
    if t_home.Valid():
        print("[UR5] Returning to home position...")
        robot.MoveJ(t_home)
    
    print("[UR5] Program completed successfully!")

# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[UR5] Program interrupted by user")
    except Exception as e:
        print(f"[UR5] Error: {e}")
        import traceback
        traceback.print_exc()

