# Team Responsibilities

## Team Structure

### Team PR2-1-1 Members

#### Sergio - UR10 Pick and Place Developer
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

#### Diego - UR5 Box Folding Developer
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
- Validate timeout and error handling
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
- `/Handshake/handshake.py`
- `/Handshake/handshake_protocol.md`
- `/Handshake/README.md`

---

## Collaboration Guidelines

### Communication
- Document all changes in `IMPROVEMENTS.md`
- Include clear descriptions of what was changed and why
- Reference specific files and line numbers when possible
- Report any issues encountered and solutions applied

### Testing
- Test individual components before integration testing
- Use the test functions provided in each module
- Report test results in documentation
- Coordinate with other team members for integration tests

### Code Standards
- Follow Python PEP 8 style guidelines
- Include docstrings for all classes and functions
- Add comments for complex logic
- Use meaningful variable and function names
- Keep functions focused and modular

### Version Control
- Commit frequently with clear commit messages
- Pull latest changes before starting work
- Resolve conflicts promptly
- Review changes before pushing

## Task Dependencies

```
Initial Setup (Complete)
    ↓
┌───────────────┬───────────────┬───────────────┐
│               │               │               │
Sergio:         Diego:          Felix:
UR10 Program    UR5 Program     Review Handshake
    │               │               │
    └───────────────┴───────────────┘
                    ↓
            Integration Testing
                    ↓
              Final Review
                    ↓
            Documentation
```

## Milestones

### Phase 1: Individual Development (Week 1)
- [ ] Sergio completes UR10 program
- [ ] Diego completes UR5 program
- [ ] Felix reviews handshake system

### Phase 2: Integration (Week 2)
- [ ] Felix tests handshake communication
- [ ] Felix coordinates integration testing
- [ ] Team resolves integration issues

### Phase 3: Testing and Documentation (Week 3)
- [ ] Complete system testing
- [ ] Final documentation updates
- [ ] Project review and sign-off

## Questions and Support

### For UR10 Questions:
Contact: Sergio

### For UR5 Questions:
Contact: Diego

### For Handshake/Integration Questions:
Contact: Felix

### For General Project Questions:
Discuss with entire team

## Updates Log

| Date | Team Member | Update |
|------|-------------|---------|
| 2024-12-25 | Setup | Initial project structure created |
| | | |
