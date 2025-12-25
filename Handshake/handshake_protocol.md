# Robot Handshake Communication Protocol

**Version:** 1.0  
**Last Updated:** December 25, 2024  
**For Review by:** Felix

## Overview
This document describes the handshake communication protocol used for synchronization between the UR10 and UR5 robots in the RoboDK project.

## Purpose
The handshake protocol ensures that both robots can work simultaneously without conflicts by coordinating their operations through signal exchange.

## Signal Types

### 1. READY
- **Purpose:** Indicates that a robot has completed initialization and is ready to begin operations
- **Sender:** Either UR10 or UR5
- **Receiver:** The other robot
- **Usage:** Sent before starting a new operation cycle

### 2. COMPLETE
- **Purpose:** Indicates that a robot has completed its current operation
- **Sender:** Either UR10 or UR5
- **Receiver:** The other robot
- **Usage:** Sent after finishing a pick/place or folding cycle

### 3. WAITING
- **Purpose:** Indicates that a robot is waiting for the other robot
- **Sender:** Either UR10 or UR5
- **Receiver:** The other robot
- **Usage:** Sent when a robot is in a waiting state

### 4. ERROR
- **Purpose:** Indicates that a robot has encountered an error
- **Sender:** Either UR10 or UR5
- **Receiver:** The other robot
- **Usage:** Sent when an error occurs that requires attention

## Communication Flow

### Workflow Sequence

```
UR10 (Pick and Place)          UR5 (Box Folding)
==================            ==================
Initialize                     Initialize
     |                              |
Send READY ------------------>     |
     |                              |
Pick Object                        |
     |                         Wait for UR10 COMPLETE
     |                              |
Place Object                       |
     |                              |
Send COMPLETE ---------------->    |
     |                         Receive COMPLETE
     |                              |
Wait for UR5 READY                 |
     |                         Fold Box
     |                              |
     |                         Send READY
     |<------------------------     |
Receive READY                      |
     |                              |
     |                         Place on Conveyor
     |                              |
[Cycle Repeats]               [Cycle Repeats]
```

## Implementation Details

### RobotHandshake Class
The `RobotHandshake` class in `handshake.py` provides the following methods:

1. **send_signal(sender, signal_type)**
   - Sends a signal from the specified robot
   - Thread-safe operation using locks
   - Timestamps each signal

2. **wait_for_signal(sender, expected_signal, timeout)**
   - Waits for a specific signal from another robot
   - Returns True if signal received, False if timeout
   - Default timeout: 30 seconds

3. **get_signal(robot_name)**
   - Retrieves the current signal from a specific robot
   - Returns None if no signal exists

4. **clear_signal(robot_name)**
   - Clears the signal for a specific robot

5. **reset_all_signals()**
   - Resets all signals (for initialization or error recovery)

## Safety Features

### Timeout Protection
- All wait operations have configurable timeouts (default: 30 seconds)
- Prevents indefinite blocking if a robot fails to send a signal

### Thread Safety
- All signal operations are protected by locks
- Ensures data integrity in multi-threaded environments

### Error Handling
- ERROR signal type for communicating failures
- Timeout warnings logged for debugging

## Usage Examples

### Example 1: UR10 Waiting for UR5
```python
# In UR10 program
handshake = RobotHandshake("UR10")
handshake.wait_for_signal("UR5", "READY")
```

### Example 2: UR5 Signaling Completion
```python
# In UR5 program
handshake = RobotHandshake("UR5")
handshake.send_signal("UR5", "COMPLETE")
```

## Testing

A test function is provided in `handshake.py`:
```bash
python Handshake/handshake.py
```

This will run through a series of tests to verify the handshake system is working correctly.

## Review Checklist for Felix

- [ ] Verify signal timing is appropriate for robot operations
- [ ] Check timeout values are sufficient for all operations
- [ ] Test error scenarios and recovery mechanisms
- [ ] Validate thread safety in concurrent operations
- [ ] Review synchronization logic for edge cases
- [ ] Test complete workflow with both robots
- [ ] Document any issues found
- [ ] Propose improvements if needed

## Future Improvements

Potential enhancements to consider:
1. Add priority levels for signals
2. Implement signal queue for multiple pending operations
3. Add heartbeat mechanism for robot health monitoring
4. Include more detailed error codes
5. Add logging to file for debugging
6. Implement signal acknowledgment mechanism

## Notes for Team

- **Sergio:** Use `wait_for_ur5_ready()` in UR10 program before critical operations
- **Diego:** Use `wait_for_ur10_complete()` in UR5 program to coordinate timing
- **Felix:** Test the handshake system thoroughly and update this document with findings
