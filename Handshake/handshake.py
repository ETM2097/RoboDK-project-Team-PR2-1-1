"""
Robot Handshake Communication Module
For Review by: Felix

This module provides communication and synchronization between UR10 and UR5 robots.
It ensures both robots can work simultaneously without conflicts.
"""

import time
from threading import Lock
from datetime import datetime


class RobotHandshake:
    """
    Handshake communication system for robot coordination.
    
    This class manages signal exchange between robots to ensure
    synchronized operations when working simultaneously.
    """
    
    # Shared state dictionary for signals (class variable for inter-robot communication)
    _signals = {}
    _lock = Lock()
    
    # Signal types
    SIGNAL_READY = "READY"
    SIGNAL_COMPLETE = "COMPLETE"
    SIGNAL_ERROR = "ERROR"
    SIGNAL_WAITING = "WAITING"
    
    def __init__(self, robot_name):
        """
        Initialize handshake for a specific robot.
        
        Args:
            robot_name: Name of the robot (e.g., "UR10" or "UR5")
        """
        self.robot_name = robot_name
        self.timeout = 30  # Default timeout in seconds
        
    def send_signal(self, sender, signal_type):
        """
        Send a signal from this robot.
        
        Args:
            sender: Name of the robot sending the signal
            signal_type: Type of signal (READY, COMPLETE, ERROR, WAITING)
        """
        with self._lock:
            timestamp = datetime.now().isoformat()
            self._signals[sender] = {
                'signal': signal_type,
                'timestamp': timestamp
            }
            print(f"[HANDSHAKE] {sender} sent signal: {signal_type} at {timestamp}")
    
    def wait_for_signal(self, sender, expected_signal, timeout=None):
        """
        Wait for a specific signal from another robot.
        
        Args:
            sender: Name of the robot to wait for
            expected_signal: Expected signal type
            timeout: Maximum time to wait in seconds (uses default if None)
            
        Returns:
            bool: True if signal received, False if timeout
        """
        if timeout is None:
            timeout = self.timeout
            
        start_time = time.time()
        
        print(f"[HANDSHAKE] {self.robot_name} waiting for {expected_signal} from {sender}...")
        
        while True:
            with self._lock:
                if sender in self._signals:
                    signal_data = self._signals[sender]
                    if signal_data['signal'] == expected_signal:
                        print(f"[HANDSHAKE] {self.robot_name} received {expected_signal} from {sender}")
                        return True
            
            # Check timeout
            if time.time() - start_time > timeout:
                print(f"[HANDSHAKE] WARNING: Timeout waiting for {expected_signal} from {sender}")
                return False
            
            # Small delay to prevent busy waiting
            time.sleep(0.1)
    
    def get_signal(self, robot_name):
        """
        Get the current signal from a specific robot.
        
        Args:
            robot_name: Name of the robot to check
            
        Returns:
            dict: Signal data or None if no signal
        """
        with self._lock:
            return self._signals.get(robot_name, None)
    
    def clear_signal(self, robot_name):
        """
        Clear the signal for a specific robot.
        
        Args:
            robot_name: Name of the robot whose signal to clear
        """
        with self._lock:
            if robot_name in self._signals:
                del self._signals[robot_name]
                print(f"[HANDSHAKE] Cleared signal for {robot_name}")
    
    def get_all_signals(self):
        """
        Get all current signals from all robots.
        
        Returns:
            dict: All robot signals
        """
        with self._lock:
            return self._signals.copy()
    
    def reset_all_signals(self):
        """Reset all signals (use for initialization or error recovery)"""
        with self._lock:
            self._signals.clear()
            print(f"[HANDSHAKE] All signals reset")


def test_handshake():
    """Test function for the handshake system"""
    print("\n" + "="*50)
    print("Testing Robot Handshake System")
    print("="*50 + "\n")
    
    # Create handshake instances for both robots
    ur10_handshake = RobotHandshake("UR10")
    ur5_handshake = RobotHandshake("UR5")
    
    # Test 1: UR10 sends READY signal
    print("Test 1: UR10 sends READY signal")
    ur10_handshake.send_signal("UR10", RobotHandshake.SIGNAL_READY)
    
    # Test 2: UR5 waits for UR10 READY signal
    print("\nTest 2: UR5 waits for UR10 READY signal")
    result = ur5_handshake.wait_for_signal("UR10", RobotHandshake.SIGNAL_READY, timeout=5)
    print(f"Result: {'Success' if result else 'Failed'}")
    
    # Test 3: UR5 sends COMPLETE signal
    print("\nTest 3: UR5 sends COMPLETE signal")
    ur5_handshake.send_signal("UR5", RobotHandshake.SIGNAL_COMPLETE)
    
    # Test 4: Check all signals
    print("\nTest 4: Check all signals")
    all_signals = ur10_handshake.get_all_signals()
    for robot, data in all_signals.items():
        print(f"  {robot}: {data['signal']} at {data['timestamp']}")
    
    # Test 5: Reset all signals
    print("\nTest 5: Reset all signals")
    ur10_handshake.reset_all_signals()
    
    print("\n" + "="*50)
    print("Handshake Test Complete")
    print("="*50 + "\n")


if __name__ == "__main__":
    test_handshake()
