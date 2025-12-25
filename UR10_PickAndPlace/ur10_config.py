"""
UR10 Robot Configuration
Responsible: Sergio

Configuration parameters for the UR10 robot operations in RoboDK.
"""


class UR10Config:
    """Configuration class for UR10 robot"""
    
    # Robot joint positions (in degrees or radians, adjust as needed)
    # Home position as joint angles [J1, J2, J3, J4, J5, J6]
    HOME_JOINTS = [0, -90, -90, -90, 90, 0]
    
    # Target names in RoboDK station
    PICK_TARGET = "UR10_PickTarget"
    PLACE_TARGET = "UR10_PlaceTarget"
    
    # Gripper settings (0-100 scale)
    GRIPPER_OPEN = 0
    GRIPPER_CLOSE = 100
    
    # Speed settings (mm/s)
    MOVE_SPEED = 150
    PICK_SPEED = 50
    
    # Safety settings
    SAFE_HEIGHT = 200  # Height in mm to move above objects before horizontal movements
    
    # Communication settings
    HANDSHAKE_TIMEOUT = 30  # seconds
    
    def __init__(self):
        """Initialize configuration"""
        pass
    
    def get_pick_target(self):
        """Get the pick target name"""
        return self.PICK_TARGET
    
    def get_place_target(self):
        """Get the place target name"""
        return self.PLACE_TARGET
    
    def get_home_joints(self):
        """Get the home joint position"""
        return self.HOME_JOINTS
