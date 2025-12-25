# RoboDK Project Overview

## Project Title
Team PR2-1-1 RoboDK Simultaneous Robot Operations

## Project Description
This project implements a coordinated system using two Universal Robots (UR10 and UR5) working simultaneously on complementary tasks. The robots communicate through a handshake protocol to ensure synchronized operations without conflicts.

## System Architecture

### Components

#### 1. UR10 Robot - Pick and Place System
- **Location:** `/UR10_PickAndPlace/`
- **Responsible:** Sergio
- **Function:** Performs pick and place operations and also implements the conveyors feeder logic
- **Key Operations:**
  - Pick objects from designated positions
  - Place objects at target locations
  - Coordinates with the conveyor feeder through handshake signals
  - Coordinate with UR5 through handshake signals

#### 2. UR5 Robot - Box Folding and Conveyor System
- **Location:** `/UR5_BoxFolding/`
- **Responsible:** Diego
- **Function:** Folds boxes and places them on conveyor
- **Key Operations:**
  - Fold boxes using the box-folder structure
  - Place folded boxes on conveyor belt
  - Coordinate with UR10 through handshake signals

#### 3. Handshake Communication System
- **Location:** `/Handshake/`
- **Responsible for Review:** Felix
- **Function:** Provides communication and synchronization between robots
- **Key Features:**
  - Signal exchange (READY, COMPLETE, ERROR, WAITING)
  - Thread-safe operations (if possible still researching)
  - Timeout protection (IF WE HAVE TIME)
  - Status tracking (optional)

## Workflow

### Overall System Flow
1. Both robots initialize and move to home positions
2. Conveyor Feeder stars spawning
3. UR10 signals WAIT for Conveyor feeder signal to set itself to READY
4. UR5 starts folding if boxes are aviable
5. UR5 places box on conveyor
6. UR10 performs pick operation when READY
7. UR10 waits for UR5 to be ready before placing
8. UR5 place and signals READY when the box reaches UR10 position
9. UR10 places object and signals COMPLETE
10. Box loses tracking from both robots and goes to closing station for final modification
11. Cycle repeats

### Synchronization Points
- **Before UR10 Place:** UR10 waits for Conveyor feeder READY signal for picking and UR5 READY signal for placing
- **Before UR5 Fold:** UR5 waits for Sensor on Boxes to be ON

## Technology Stack
- **Programming Language:** Python 3
- **Robot Platform:** RoboDK
- **Robot Models:** UR10, UR5 (Universal Robots)
- **Communication:** Custom handshake protocol with threading (maybe if not ParamSet() from RoboDK)

## Directory Structure
```
RoboDK-project-Team-PR2-1-1/
├── UR10_PickAndPlace/
│   ├── README.md
│   ├── ur10_program.py
│   └── ur10_config.py
├── UR5_BoxFolding/
│   ├── README.md
│   ├── ur5_program.py
│   └── ur5_config.py
├── Handshake/
│   ├── README.md
│   ├── handshake.py
│   └── handshake_protocol.md
├── Documentation/
│   ├── README.md
│   ├── PROJECT_OVERVIEW.md (this file)
│   ├── TEAM_RESPONSIBILITIES.md
│   └── IMPROVEMENTS.md
└── README.md
```

## Safety Considerations
1. Both robots operate at safe speeds
2. Timeout protection prevents indefinite waiting (optional)
3. Error signals allow for fault detection and recovery (mandatory for debugging)
4. Handshake protocol ensures no simultaneous access to shared workspace/material

## Testing
Each component can be tested independently:
- **UR10 Program:** `python UR10_PickAndPlace/ur10_program.py`
- **UR5 Program:** `python UR5_BoxFolding/ur5_program.py`
- **Handshake System:** `python Handshake/handshake.py`

## Future Enhancements
1. Add RoboDK integration for actual robot control
2. Implement error recovery mechanisms
3. Add logging system for operation history
4. Create visualization dashboard
5. Add more sophisticated synchronization patterns
6. Implement collision detection and avoidance

## Contact Information
- **Project Leader:** Enric
- **UR10 Developer:** Sergio
- **UR5 Developer:** Diego
- **Integration Reviewer:** Felix

## Version History
- **v1.0** (December 25, 2024) - Initial project setup with basic structure and handshake protocol
