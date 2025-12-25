"""
UR5 Box Folding and Conveyor Program
Responsible: Diego

This RoboDK program controls the UR5 robot for box folding operations
and placing boxes on the conveyor belt, coordinating with the UR10 robot.

This script is designed to run within RoboDK environment.
"""

from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
import sys
import os

# Add parent directory to path to import handshake module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Handshake.handshake import RobotHandshake
from UR5_BoxFolding.ur5_config import UR5Config


class UR5BoxFolding:
    """UR5 Robot controller for box folding and conveyor operations"""
    
    def __init__(self):
        self.config = UR5Config()
        self.handshake = RobotHandshake("UR5")
        
        # Connect to RoboDK
        self.RDK = Robolink()
        
        # Get the UR5 robot
        self.robot = self.RDK.Item('UR5', ITEM_TYPE_ROBOT)
        if not self.robot.Valid():
            raise Exception("UR5 robot not found in RoboDK station")
        
        # Get reference frame and tool
        self.frame = self.RDK.Item('UR5 Base')
        self.tool = self.robot.PoseTool()
        
        print(f"[UR5] Connected to RoboDK")
        print(f"[UR5] Robot: {self.robot.Name()}")
        
    def initialize(self):
        """Initialize the UR5 robot"""
        print(f"[UR5] Initializing robot...")
        
        # Move to home position
        home_joints = self.config.HOME_JOINTS
        self.robot.MoveJ(home_joints)
        
        print(f"[UR5] Robot initialized at home position")
        
    def fold_box(self, box_id):
        """
        Fold a box according to the folding sequence
        
        Args:
            box_id: Identifier for the box being folded
        """
        print(f"[UR5] Starting box folding sequence for box {box_id}")
        
        # Get folding targets from RoboDK station
        folding_targets = self.config.get_folding_targets()
        
        # Folding steps
        for i, (step_name, target_name) in enumerate(zip(self.config.FOLDING_SEQUENCE, folding_targets), 1):
            print(f"[UR5] Folding step {i}: {step_name}")
            
            # Get the target from RoboDK station
            target = self.RDK.Item(target_name, ITEM_TYPE_TARGET)
            if target.Valid():
                # Move to folding position
                self.robot.MoveL(target)
                # Pause briefly to simulate folding action
                pause(0.5)
            else:
                print(f"[UR5] Warning: Target '{target_name}' not found, skipping step")
            
        print(f"[UR5] Box {box_id} folded successfully")
        
    def place_on_conveyor(self, box_id):
        """
        Place the folded box on the conveyor belt
        
        Args:
            box_id: Identifier for the box
        """
        print(f"[UR5] Moving box {box_id} to conveyor")
        
        # Get the conveyor target from RoboDK station
        conveyor_target = self.RDK.Item(self.config.CONVEYOR_TARGET, ITEM_TYPE_TARGET)
        if not conveyor_target.Valid():
            print(f"[UR5] Warning: Conveyor target not found, using default position")
            conveyor_target = self.robot.Pose()
        
        # Move above the conveyor position
        approach_pose = conveyor_target.Pose() * transl(0, 0, self.config.SAFE_HEIGHT)
        self.robot.MoveJ(approach_pose)
        
        # Move down to conveyor
        self.robot.MoveL(conveyor_target)
        
        # Release box (simulate)
        print(f"[UR5] Releasing box on conveyor...")
        # TODO: Implement actual gripper control
        # self.open_gripper()
        
        # Move back up
        self.robot.MoveL(approach_pose)
        
        # Wait for conveyor to move box
        pause(self.config.CONVEYOR_WAIT_TIME)
        
        print(f"[UR5] Box {box_id} placed on conveyor successfully")
        
    def wait_for_ur10_complete(self):
        """Wait for UR10 to complete its operation"""
        print("[UR5] Waiting for UR10 to complete operation...")
        self.handshake.wait_for_signal("UR10", RobotHandshake.SIGNAL_COMPLETE)
        print("[UR5] UR10 operation complete, proceeding...")
        
    def signal_ready(self):
        """Signal that UR5 is ready for next operation"""
        print("[UR5] Signaling ready status...")
        self.handshake.send_signal("UR5", RobotHandshake.SIGNAL_READY)
        
    def run_folding_cycle(self, box_id):
        """
        Execute a complete box folding and conveyor placement cycle
        
        Args:
            box_id: Identifier for the box
        """
        print(f"[UR5] Starting folding cycle for box {box_id}...")
        
        # Wait for UR10 to complete its operation
        self.wait_for_ur10_complete()
        
        # Fold the box
        self.fold_box(box_id)
        
        # Signal ready for coordination
        self.signal_ready()
        
        # Place box on conveyor
        self.place_on_conveyor(box_id)
        
        print(f"[UR5] Folding cycle for box {box_id} completed")


def main():
    """Main function to run UR5 box folding program"""
    print("="*50)
    print("UR5 Box Folding and Conveyor Program - RoboDK")
    print("Responsible: Diego")
    print("="*50)
    
    try:
        robot = UR5BoxFolding()
        robot.initialize()
        
        # Run a test cycle
        robot.run_folding_cycle(box_id=1)
        
    except Exception as e:
        print(f"[UR5] Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
