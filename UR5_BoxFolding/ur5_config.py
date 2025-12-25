"""
UR5 Robot Configuration
Responsible: Diego

Configuration parameters for the UR5 robot box folding and conveyor operations in RoboDK.
"""


class UR5Config:
    """Configuration class for UR5 robot"""
    
    # Robot joint positions (in degrees or radians, adjust as needed)
    # Home position as joint angles [J1, J2, J3, J4, J5, J6]
    HOME_JOINTS = [0, -90, -90, -90, 90, 0]
    
    # Target names in RoboDK station
    FOLDING_TARGET_1 = "UR5_Fold1_Bottom"
    FOLDING_TARGET_2 = "UR5_Fold2_Left"
    FOLDING_TARGET_3 = "UR5_Fold3_Right"
    FOLDING_TARGET_4 = "UR5_Fold4_Top"
    CONVEYOR_TARGET = "UR5_ConveyorTarget"
    
    # Folding sequence steps
    FOLDING_SEQUENCE = [
        "Fold bottom flap",
        "Fold left side",
        "Fold right side",
        "Fold top flap and seal"
    ]
    
    # Gripper settings (0-100 scale)
    GRIPPER_OPEN = 0
    GRIPPER_CLOSE = 80
    
    # Speed settings (mm/s)
    MOVE_SPEED = 120
    FOLDING_SPEED = 30
    
    # Safety settings
    SAFE_HEIGHT = 200  # Height in mm to move above objects before horizontal movements
    
    # Communication settings
    HANDSHAKE_TIMEOUT = 30  # seconds
    
    # Conveyor settings
    CONVEYOR_SPEED = 50  # mm/s
    CONVEYOR_WAIT_TIME = 2  # seconds to wait after placing box
    
    def __init__(self):
        """Initialize configuration"""
        pass
    
    def get_folding_sequence(self):
        """Get the folding sequence steps"""
        return self.FOLDING_SEQUENCE
    
    def get_folding_targets(self):
        """Get the list of folding target names"""
        return [
            self.FOLDING_TARGET_1,
            self.FOLDING_TARGET_2,
            self.FOLDING_TARGET_3,
            self.FOLDING_TARGET_4
        ]
    
    def get_conveyor_target(self):
        """Get the conveyor target name"""
        return self.CONVEYOR_TARGET
    
    def get_home_joints(self):
        """Get the home joint position"""
        return self.HOME_JOINTS
