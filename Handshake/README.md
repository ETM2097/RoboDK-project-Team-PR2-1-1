# Handshake Communication Module

**Responsible for Review:** Felix

## Purpose
This folder contains the handshake communication system that enables the UR10 and UR5 robots to coordinate and work simultaneously.

## Description
The handshake module provides:
- Signal sending and receiving between robots
- Synchronization mechanisms to prevent conflicts
- Status tracking for both robots
- Error handling and timeout management

## Files
- `handshake.py` - Main handshake communication implementation
- `handshake_protocol.md` - Documentation of the communication protocol

## Integration
Both UR10 and UR5 programs import and use this handshake module to:
- Signal when they are ready to start operations
- Wait for the other robot to complete critical operations
- Signal completion of their own operations
- Maintain synchronized workflow

## Instructions for Felix
1. Review the handshake implementation in `handshake.py`
2. Check the protocol documentation in `handshake_protocol.md`
3. Test the communication between robots
4. Correct any synchronization issues
5. Document findings and improvements in `/Documentation`
