# Team Responsibilities

## Team Structure

### Team PR2-1-1 Members

#### Enric - Team Leader, Documentation manager and Reviewer
**Primary Responsibilities:**
- Write and mantain the documentation
- Review the whole porject daily in order to proper planning next moves
- Guide the other project collaborators properly in order to fullfill milestone dates

**Please contact him to resolve any question you have**

#### Sergio - UR10 Pick and Place Developer + Conveyor Logic
**Primary Responsibilities:**
- Develop and maintain the UR10 robot program
- Implement pick and place logic
- Configure UR10 robot parameters
- Integrate handshake communication in UR10 program
- Test UR10 operations independently
- Document UR10 improvements and issues

**Deliverables:**
- [ ] Complete `ur10_program.py` with pick and place logic
- [ ] Configure optimal parameters in `ur10_config.py`
- [ ] Implement handshake integration
- [ ] Test and validate UR10 operations
- [ ] Document improvements in `/Documentation/IMPROVEMENTS.md`

**Key Files:**
- `/UR10_PickAndPlace/ur10_program.py`
- `/UR10_PickAndPlace/ur10_config.py`
- `/UR10_PickAndPlace/README.md`

---

#### Diego - UR5 Box Folding Developer + Spawning Logic
**Primary Responsibilities:**
- Develop and maintain the UR5 robot program
- Implement box folding sequence
- Implement conveyor placement logic
- Configure UR5 robot parameters
- Integrate handshake communication in UR5 program
- Test UR5 operations independently
- Document UR5 improvements and issues

**Deliverables:**
- [ ] Complete `ur5_program.py` with folding and conveyor logic
- [ ] Configure optimal parameters in `ur5_config.py`
- [ ] Implement handshake integration
- [ ] Test and validate UR5 operations
- [ ] Document improvements in `/Documentation/IMPROVEMENTS.md`

**Key Files:**
- `/UR5_BoxFolding/ur5_program.py`
- `/UR5_BoxFolding/ur5_config.py`
- `/UR5_BoxFolding/README.md`

---

#### Felix - Integration and Communication Specialist
**Primary Responsibilities:**
- Review and test the handshake communication system
- Verify synchronization between UR10 and UR5
- Identify and correct communication issues
- Test complete integrated system
- Validate timeout (optional) and error handling
- Document integration test results
- Propose improvements to handshake protocol

**Deliverables:**
- [ ] Test handshake communication system
- [ ] Verify UR10-UR5 synchronization
- [ ] Test error scenarios and recovery
- [ ] Validate complete workflow
- [ ] Document findings in `/Documentation/IMPROVEMENTS.md`
- [ ] Update `/Handshake/handshake_protocol.md` if needed
- [ ] Correct any synchronization issues found

**Key Files:**
- `/Handshake/handshake.py` Where the semaphores will be properly updated
- `/Handshake/handshake_protocol.md`
- `/Handshake/README.md`

---

## Collaboration Guidelines

### Communication
- Document all changes in `IMPROVEMENTS.md` 
- Include clear descriptions of what was changed and why
- Reference specific files and line numbers when possible
- Report any issues encountered and solutions applied to Enric

### Testing
- Test individual components before integration testing
- Report test results in documentation
- Coordinate with other team members for integration tests, Ex. Testing start/stop of the object following

### Code Standards
- Follow Python coding guidelines
- Include proper documentation for all classes and functions
- Add comments for complex logic at the top of the logic
- Use meaningful variable and function names, Ex. `baseFrameConveyor`
- Keep functions focused and modular, as we may use them more than once

### Version Control
- Commit frequently with clear commit messages
- Pull latest changes before starting work `MANDATORY`
- Contact Enric in case you have a conflict for correctly resolve it
- Review changes before pushing


## Milestones

### Phase 1: Individual Development (Up to 26/12/25)
- [ ] Sergio completes UR10 program with the conveyor spawning and proper pick and place logic
- [ ] Diego completes UR5 program with the proper picking, folding, placing and spawning logic
- [ ] Felix reviews handshake system making sure programs starts and stops when they have to (no placing before box for example)

### Phase 2: Integration (Up to 28/12/25)
- [ ] Felix tests handshake communication
- [ ] Felix coordinates integration testing
- [ ] Team resolves integration issues by making changes required by Felix

### Phase 3: Testing and Documentation (Up to 31/12/25)
- [ ] Felix Complete system testing
- [ ] Enric reviews final documentation updates
- [ ] Enric makes the full project review and validation

### Phase 4: Writing final documentation and presentation making (Up to 05/12/25)
- [ ] Felix and Sergio creates the presentation for PRR
- [ ] Diego is in charge of generating the timelines and other requirements for PR2 part of the project
- [ ] Enric writes the documentation needed for PRR
- [ ] Felix and sergio review the documentations and double-checks them

## Questions and Support

### For UR10 Questions:
Contact: Sergio

### For UR5 Questions:
Contact: Diego

### For Handshake/Integration Questions:
Contact: Felix

### For General Project Questions:
Contact: Enric

## Updates Log

| Date | Team Member | Update |
|------|-------------|---------|
| 2025-12-25 // 12:00 | Enric | Initial project structure created |
| 2025-12-25 // 18:30 | Enric | Changed main implementation issuses for easier implementation |
| | | |
