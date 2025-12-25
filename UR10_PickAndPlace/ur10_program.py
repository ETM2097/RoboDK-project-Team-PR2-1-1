"""
UR10 Pick and Place Program
Responsible: Sergio

This program controls the UR10 robot for pick and place operations
and coordinates with the UR5 robot through handshake signals.
"""

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
        self.current_position = None
        
    def initialize(self):
        """Initialize the UR10 robot"""
        print(f"[UR10] Initializing robot...")
        print(f"[UR10] Home position: {self.config.HOME_POSITION}")
        # TODO: Initialize RoboDK connection
        # TODO: Move to home position
        
    def pick_object(self, object_position):
        """
        Pick an object from the specified position
        
        Args:
            object_position: Coordinates [x, y, z] of the object
        """
        print(f"[UR10] Moving to pick position: {object_position}")
        # TODO: Move to object position
        # TODO: Close gripper
        print(f"[UR10] Object picked successfully")
        
    def place_object(self, target_position):
        """
        Place the object at the specified target position
        
        Args:
            target_position: Coordinates [x, y, z] for placement
        """
        print(f"[UR10] Moving to place position: {target_position}")
        # TODO: Move to target position
        # TODO: Open gripper
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
        
        # Pick object
        self.pick_object(self.config.PICK_POSITION)
        
        # Place object
        self.place_object(self.config.PLACE_POSITION)
        
        # Signal completion
        self.signal_operation_complete()
        
        # Wait for UR5 to finish before next cycle
        print("[UR10] Waiting for UR5 to finish folding...")
        self.wait_for_ur5_ready()
        
        print("[UR10] Pick and place cycle completed")


def main():
    """Main function to run UR10 pick and place program"""
    print("="*50)
    print("UR10 Pick and Place Program")
    print("Responsible: Sergio")
    print("="*50)
    
    robot = UR10PickAndPlace()
    robot.initialize()
    
    # Run a test cycle
    robot.run_pick_and_place_cycle()


if __name__ == "__main__":
    main()
