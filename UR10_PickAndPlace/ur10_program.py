"""
UR10 Pick and Place Program
Responsible: Sergio

This RoboDK program controls the UR10 robot for pick and place operations
and coordinates with the UR5 robot through handshake signals.

This script is designed to run within RoboDK environment.
"""

from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
import sys
import os

# Add parent directory to path to import handshake module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Handshake.handshake import RobotHandshake
from UR10_PickAndPlace.ur10_config import UR10Config


class UR10PickAndPlace:
    """UR10 Robot controller for pick and place operations"""
    
    def __init__(self):
        self.config = UR10Config()
        self.handshake = RobotHandshake("UR10")
        
        # Connect to RoboDK
        self.RDK = Robolink()
        
        # Get the UR10 robot
        self.robot = self.RDK.Item('UR10', ITEM_TYPE_ROBOT)
        if not self.robot.Valid():
            raise Exception("UR10 robot not found in RoboDK station")
        
        # Get reference frame and tool
        self.frame = self.RDK.Item('UR10 Base')
        self.tool = self.robot.PoseTool()
        
        print(f"[UR10] Connected to RoboDK")
        print(f"[UR10] Robot: {self.robot.Name()}")
        
    def initialize(self):
        """Initialize the UR10 robot"""
        print(f"[UR10] Initializing robot...")
        
        # Move to home position
        home_joints = self.config.HOME_JOINTS
        self.robot.MoveJ(home_joints)
        
        print(f"[UR10] Robot initialized at home position")
        
    def pick_object(self, target_name):
        """
        Pick an object from the specified target
        
        Args:
            target_name: Name of the target/object in RoboDK station
        """
        print(f"[UR10] Moving to pick object: {target_name}")
        
        # Get the target from RoboDK station
        target = self.RDK.Item(target_name, ITEM_TYPE_TARGET)
        if not target.Valid():
            print(f"[UR10] Warning: Target '{target_name}' not found, using default position")
            target = self.robot.Pose()
        
        # Move above the object
        approach_pose = target.Pose() * transl(0, 0, self.config.SAFE_HEIGHT)
        self.robot.MoveJ(approach_pose)
        
        # Move down to pick position
        self.robot.MoveL(target)
        
        # Close gripper (simulate)
        print(f"[UR10] Closing gripper...")
        # TODO: Implement actual gripper control
        # self.close_gripper()
        
        # Move back up
        self.robot.MoveL(approach_pose)
        
        print(f"[UR10] Object picked successfully")
        
    def place_object(self, target_name):
        """
        Place the object at the specified target position
        
        Args:
            target_name: Name of the placement target in RoboDK station
        """
        print(f"[UR10] Moving to place position: {target_name}")
        
        # Get the target from RoboDK station
        target = self.RDK.Item(target_name, ITEM_TYPE_TARGET)
        if not target.Valid():
            print(f"[UR10] Warning: Target '{target_name}' not found, using default position")
            target = self.robot.Pose()
        
        # Move above the placement position
        approach_pose = target.Pose() * transl(0, 0, self.config.SAFE_HEIGHT)
        self.robot.MoveJ(approach_pose)
        
        # Move down to place position
        self.robot.MoveL(target)
        
        # Open gripper (simulate)
        print(f"[UR10] Opening gripper...")
        # TODO: Implement actual gripper control
        # self.open_gripper()
        
        # Move back up
        self.robot.MoveL(approach_pose)
        
        print(f"[UR10] Object placed successfully")
        
    def wait_for_ur5_ready(self):
        """Wait for UR5 to signal it's ready"""
        print("[UR10] Waiting for UR5 to be ready...")
        self.handshake.wait_for_signal("UR5", RobotHandshake.SIGNAL_READY)
        print("[UR10] UR5 is ready, proceeding...")
        
    def signal_operation_complete(self):
        """Signal that UR10 has completed its operation"""
        print("[UR10] Signaling operation complete...")
        self.handshake.send_signal("UR10", RobotHandshake.SIGNAL_COMPLETE)
        
    def run_pick_and_place_cycle(self):
        """Execute a complete pick and place cycle"""
        print("[UR10] Starting pick and place cycle...")
        
        # Signal ready to start
        self.handshake.send_signal("UR10", RobotHandshake.SIGNAL_READY)
        
        # Pick object from pick target
        self.pick_object(self.config.PICK_TARGET)
        
        # Place object at place target
        self.place_object(self.config.PLACE_TARGET)
        
        # Signal completion
        self.signal_operation_complete()
        
        # Wait for UR5 to finish before next cycle
        print("[UR10] Waiting for UR5 to finish folding...")
        self.wait_for_ur5_ready()
        
        print("[UR10] Pick and place cycle completed")


def main():
    """Main function to run UR10 pick and place program"""
    print("="*50)
    print("UR10 Pick and Place Program - RoboDK")
    print("Responsible: Sergio")
    print("="*50)
    
    try:
        robot = UR10PickAndPlace()
        robot.initialize()
        
        # Run a test cycle
        robot.run_pick_and_place_cycle()
        
    except Exception as e:
        print(f"[UR10] Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
