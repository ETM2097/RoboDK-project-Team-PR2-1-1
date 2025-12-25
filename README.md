# RoboDK Project - Team PR2-1-1

## Project Description
Working repository for Team PR2-1-1's RoboDK project featuring coordinated operation of UR10 and UR5 robots using RoboDK simulation and control software.

**This repository provides TEMPLATES that team members should build upon to implement their robot programs.**

## Team Members
- **Sergio** - UR10 Pick and Place Programming
- **Diego** - UR5 Box Folding and Conveyor Programming
- **Felix** - Handshake Communication Review and Integration

## Project Structure

### 🤖 Robot Program Templates (RoboDK Compatible)

#### UR10_PickAndPlace/
**Responsible:** Sergio  
**TEMPLATE** for UR10 robot pick and place operations.
- `ur10_program.py` - RoboDK program template with basic structure
- `README.md` - Detailed setup instructions and template guide

**Sergio should:**
- Set up RoboDK station with UR10 and targets
- Build upon the template to implement complete logic
- Implement gripper control
- Test and refine the program

#### UR5_BoxFolding/
**Responsible:** Diego  
**TEMPLATE** for UR5 robot box folding and conveyor operations.
- `ur5_program.py` - RoboDK program template with basic structure
- `README.md` - Detailed setup instructions and template guide

**Diego should:**
- Set up RoboDK station with UR5 and targets
- Build upon the template to implement complete logic
- Implement box folding actions
- Test and refine the program

### 🤝 Communication System

#### Handshake/
**Responsible for Review:** Felix  
Communication module for robot synchronization and coordination.
- `handshake.py` - Handshake implementation (ready to use)
- `handshake_protocol.md` - Protocol documentation
- `README.md` - Module documentation

### 📚 Documentation/
Shared documentation for team improvements and collaboration.
- `PROJECT_OVERVIEW.md` - Complete project description
- `TEAM_RESPONSIBILITIES.md` - Team roles and tasks
- `IMPROVEMENTS.md` - Log of changes and improvements
- `README.md` - Documentation guide

## Quick Start

### Prerequisites
- **RoboDK** software installed (download from https://robodk.com/)
- Python 3.x
- RoboDK API for Python (included with RoboDK installation)

### Setting Up Your RoboDK Station

#### For UR10 (Sergio):
1. Open RoboDK
2. Add a UR10 robot to your station (name it **"UR10"**)
3. Create the following targets by moving the robot to desired positions:
   - `UR10_Home` - Home/starting position
   - `UR10_PrePick` - Pre-pick approach position
   - `UR10_Pick` - Pick position
   - `UR10_PrePlace` - Pre-place approach position
   - `UR10_Place` - Place position
4. Load `UR10_PickAndPlace/ur10_program.py` into RoboDK
5. Build upon the template to implement your specific logic

See `UR10_PickAndPlace/README.md` for detailed instructions.

#### For UR5 (Diego):
1. Open RoboDK
2. Add a UR5 robot to your station (name it **"UR5"**)
3. Create the following targets by moving the robot to desired positions:
   - `UR5_Home` - Home/starting position
   - `UR5_Fold1` - Position for folding bottom flap
   - `UR5_Fold2` - Position for folding left side
   - `UR5_Fold3` - Position for folding right side
   - `UR5_Fold4` - Position for folding top flap and seal
   - `UR5_ConveyorPlace` - Position to place box on conveyor
4. Load `UR5_BoxFolding/ur5_program.py` into RoboDK
5. Build upon the template to implement your specific logic

See `UR5_BoxFolding/README.md` for detailed instructions.

### Running Robot Programs in RoboDK

**Option 1: Within RoboDK**
1. Right-click on robot → Add Program → Python
2. Load the program file (ur10_program.py or ur5_program.py)
3. Double-click the program to run it

**Option 2: From Command Line** (RoboDK must be running)
```bash
# Run UR10 program
python UR10_PickAndPlace/ur10_program.py

# Run UR5 program
python UR5_BoxFolding/ur5_program.py
```

### Testing Handshake System

Test the handshake communication system independently:
```bash
python Handshake/handshake.py
```

## How It Works

1. **UR10** performs pick and place operations using RoboDK targets
2. **UR5** folds boxes and places them on the conveyor using RoboDK targets
3. Both robots use **handshake signals** to coordinate timing
4. The handshake system ensures simultaneous operation without conflicts

## Workflow

```
UR10: Initialize → Signal READY → Pick → Place → Signal COMPLETE → Wait for UR5 → [Repeat]
                                                          ↓
UR5:  Initialize → Wait for UR10 COMPLETE → Fold → Signal READY → Conveyor → [Repeat]
```

## Documentation

For detailed information, see:
- [Project Overview](Documentation/PROJECT_OVERVIEW.md) - Complete system architecture
- [Team Responsibilities](Documentation/TEAM_RESPONSIBILITIES.md) - Roles and tasks
- [Handshake Protocol](Handshake/handshake_protocol.md) - Communication details
- [Improvements Log](Documentation/IMPROVEMENTS.md) - Change tracking

## Contributing

Team members should:
1. Set up their RoboDK station with required robots and targets
2. Work on their assigned robot program
3. Use the handshake module for robot coordination
4. Document all improvements in `Documentation/IMPROVEMENTS.md`
5. Test changes in RoboDK simulation before committing

## Requirements
- **RoboDK** (simulation and control software)
- Python 3.x
- RoboDK API for Python (robolink, robodk modules)

## Project Status

- [x] Project structure created
- [x] **UR10 RoboDK program TEMPLATE created** - Sergio should build upon this
- [x] **UR5 RoboDK program TEMPLATE created** - Diego should build upon this
- [x] Handshake communication system implemented
- [x] Documentation framework established
- [ ] UR10 RoboDK station setup and program implementation by Sergio
- [ ] UR5 RoboDK station setup and program implementation by Diego
- [ ] Handshake system reviewed by Felix
- [ ] Integration testing in RoboDK completed
- [ ] Final documentation completed

## Important Notes

- **These are TEMPLATES** - Team members should build upon them to implement complete functionality
- Programs follow RoboDK patterns with `from robodk import robolink, robomath`
- Simple, direct code structure without complex classes
- Use `RDK.Item()` to get robots and targets
- Configuration parameters are at the top of each file for easy adjustment
- Placeholders (TODO comments) indicate where team members should add their specific logic

## For Instructors/Reviewers

The provided templates follow RoboDK best practices:
- Use official RoboDK API (`robolink`, `robomath`)
- Simple procedural structure easy to understand and modify
- Clear helper functions for common operations
- Handshake coordination integrated
- Comments indicating where to add specific implementations

## License
Team PR2-1-1 Project

## Contact
For questions, refer to [Team Responsibilities](Documentation/TEAM_RESPONSIBILITIES.md) for appropriate team member contacts.

Test handshake system:
```bash
python Handshake/handshake.py
```

## How It Works

1. **UR10** performs pick and place operations
2. **UR5** folds boxes and places them on the conveyor
3. Both robots use **handshake signals** to coordinate timing
4. The handshake system ensures simultaneous operation without conflicts

## Workflow

```
UR10: Initialize → Signal READY → Pick → Wait for UR5 → Place → Signal COMPLETE → [Repeat]
                                                    ↓
UR5:  Initialize → Wait for UR10 COMPLETE → Fold → Signal READY → Conveyor → [Repeat]
```

## Documentation

For detailed information, see:
- [Project Overview](Documentation/PROJECT_OVERVIEW.md) - Complete system architecture
- [Team Responsibilities](Documentation/TEAM_RESPONSIBILITIES.md) - Roles and tasks
- [Handshake Protocol](Handshake/handshake_protocol.md) - Communication details
- [Improvements Log](Documentation/IMPROVEMENTS.md) - Change tracking

## Contributing

Team members should:
1. Work on their assigned robot program or review task
2. Use the handshake module for robot coordination
3. Document all improvements in `Documentation/IMPROVEMENTS.md`
4. Test changes before committing
5. Follow the collaboration guidelines in team documentation

## Requirements
- Python 3.x
- RoboDK (for actual robot control)

## Project Status

- [x] Project structure created
- [x] UR10 program template created
- [x] UR5 program template created
- [x] Handshake communication system implemented
- [x] Documentation framework established
- [ ] UR10 program completed by Sergio
- [ ] UR5 program completed by Diego
- [ ] Handshake system reviewed by Felix
- [ ] Integration testing completed
- [ ] Final documentation completed

## License
Team PR2-1-1 Project

## Contact
For questions, refer to [Team Responsibilities](Documentation/TEAM_RESPONSIBILITIES.md) for appropriate team member contacts.