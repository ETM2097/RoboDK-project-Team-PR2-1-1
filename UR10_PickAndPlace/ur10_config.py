"""
UR10 Robot Configuration
Responsible: Sergio

Configuration parameters for the UR10 robot operations.
"""


class UR10Config:
    """Configuration class for UR10 robot"""
    
    # Robot positions (x, y, z) in millimeters
    HOME_POSITION = [0, -500, 300]
    PICK_POSITION = [200, -400, 50]
    PLACE_POSITION = [400, -200, 100]
    
    # Gripper settings
    GRIPPER_OPEN = 0
    GRIPPER_CLOSE = 100
    
    # Speed settings (mm/s)
    MOVE_SPEED = 150
    PICK_SPEED = 50
    
    # Safety settings
    SAFE_HEIGHT = 200  # Height to move to before horizontal movements
    
    # Communication settings
    HANDSHAKE_TIMEOUT = 30  # seconds
    
    def __init__(self):
        """Initialize configuration"""
        pass
    
    def get_pick_position(self):
        """Get the pick position coordinates"""
        return self.PICK_POSITION
    
    def get_place_position(self):
        """Get the place position coordinates"""
        return self.PLACE_POSITION
    
    def get_home_position(self):
        """Get the home position coordinates"""
        return self.HOME_POSITION
