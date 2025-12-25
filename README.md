# RoboDK Project - Team PR2-1-1

## Project Description
Working repository for Team PR2-1-1's RoboDK project featuring coordinated operation of UR10 and UR5 robots.

## Team Members
- **Sergio** - UR10 Pick and Place Programming
- **Diego** - UR5 Box Folding and Conveyor Programming
- **Felix** - Handshake Communication Review and Integration

## Project Structure

### 🤖 Robot Programs

#### UR10_PickAndPlace/
**Responsible:** Sergio  
Program for UR10 robot to perform pick and place operations.
- `ur10_program.py` - Main robot control program
- `ur10_config.py` - Configuration parameters
- `README.md` - Documentation

#### UR5_BoxFolding/
**Responsible:** Diego  
Program for UR5 robot to fold boxes and place them on the conveyor.
- `ur5_program.py` - Main robot control program
- `ur5_config.py` - Configuration parameters
- `README.md` - Documentation

### 🤝 Communication System

#### Handshake/
**Responsible for Review:** Felix  
Communication module for robot synchronization and coordination.
- `handshake.py` - Handshake implementation
- `handshake_protocol.md` - Protocol documentation
- `README.md` - Module documentation

### 📚 Documentation/
Shared documentation for team improvements and collaboration.
- `PROJECT_OVERVIEW.md` - Complete project description
- `TEAM_RESPONSIBILITIES.md` - Team roles and tasks
- `IMPROVEMENTS.md` - Log of changes and improvements
- `README.md` - Documentation guide

## Quick Start

### Running Individual Robot Programs

Test UR10 program:
```bash
python UR10_PickAndPlace/ur10_program.py
```

Test UR5 program:
```bash
python UR5_BoxFolding/ur5_program.py
```

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