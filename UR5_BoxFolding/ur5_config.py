"""
UR5 Robot Configuration
Responsible: Diego

Configuration parameters for the UR5 robot box folding and conveyor operations.
"""


class UR5Config:
    """Configuration class for UR5 robot"""
    
    # Robot positions (x, y, z) in millimeters
    HOME_POSITION = [0, 500, 300]
    BOX_PICKUP_POSITION = [-200, 400, 50]
    FOLDING_POSITION = [-200, 300, 100]
    CONVEYOR_POSITION = [-400, 100, 150]
    
    # Folding sequence steps
    FOLDING_SEQUENCE = [
        "Fold bottom flap",
        "Fold left side",
        "Fold right side",
        "Fold top flap and seal"
    ]
    
    # Gripper settings
    GRIPPER_OPEN = 0
    GRIPPER_CLOSE = 80
    
    # Speed settings (mm/s)
    MOVE_SPEED = 120
    FOLDING_SPEED = 30
    
    # Safety settings
    SAFE_HEIGHT = 200  # Height to move to before horizontal movements
    
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
    
    def get_conveyor_position(self):
        """Get the conveyor position coordinates"""
        return self.CONVEYOR_POSITION
    
    def get_home_position(self):
        """Get the home position coordinates"""
        return self.HOME_POSITION
