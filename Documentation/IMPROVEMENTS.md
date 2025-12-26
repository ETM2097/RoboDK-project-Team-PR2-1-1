# Improvements and Changes Log

## Purpose
This document tracks all improvements, changes, and fixes made to the RoboDK project by team members. This file is directly managed and revised by Enric, you have the template for a new entry on the bottom of this file. No need to fill the table, that is Enric's job.

## How to Use This Document
When you make improvements or changes:
1. Add a new entry under the appropriate section
2. Include the date, your name, and a clear description
3. Reference specific files or functions affected
4. Describe the reason for the change and the benefit

---

## UR10 Pick and Place Improvements
**Developer:** Sergio

### [Date] - [Description]
**Files Modified:**
- List files changed

**Changes Made:**
- Describe what was changed

**Reason:**
- Explain why the change was made

**Testing:**
- Describe how the change was tested

**Results:**
- Report the outcome

---

## UR5 Box Folding Improvements
**Developer:** Diego

### [Date] - [Description]
**Files Modified:**
- List files changed

**Changes Made:**
- Describe what was changed

**Reason:**
- Explain why the change was made

**Testing:**
- Describe how the change was tested

**Results:**
- Report the outcome

---

## Handshake Communication Improvements
**Reviewer:** Felix

### [Date] - [Description]
**Files Modified:**
- List files changed

**Issues Found:**
- Describe any issues discovered

**Corrections Made:**
- Describe corrections applied

**Testing:**
- Describe integration tests performed

**Results:**
- Report the outcome

---

## Integration and System-Wide Improvements
**Team:** All Members

### [Date] - [Description]
**Scope:**
- Describe what components were affected

**Changes Made:**
- Describe system-wide changes

**Testing:**
- Describe integration testing

**Results:**
- Report the outcome

---

## Known Issues

### Active Issues
| Issue # | Date | Reporter | Description | Status | Assigned To |
|---------|------|----------|-------------|--------|-------------|
| 1. Problem with placing hights | 25/12/25 | Enric | There is a problem in the logic of placing the material inside the box, it seems to be inversed, we need further checking in order to correct the logic beind it | Pending to review solution | Sergio |
| 2. Wrong point on UR5 | 25/12/25 | Enric | We need to finish the UR5 folding sequence correctly, please, update as soon as possible | Pending updates | Diego | 
| 3. Pending parameters in the handshake protocol | 26/12/25 | Enric | We need to add the newly agreed parameters to the monitor in order to add the funcionalities described on the meeting | Work ongoing | Felix |

### Resolved Issues
| Issue # | Date Reported | Date Resolved | Description | Resolution | Resolved By |
|---------|---------------|---------------|-------------|------------|-------------|
| - | - | - | - | - | - |

---

## Suggestions for Future Work

### Performance Improvements
- List potential performance enhancements
    - Potential improvement on the boxConveyor movement as it must move one by one all the boxes due an implemented functionality

### Feature Additions
- List potential new features

### Code Quality
- List potential code quality improvements

---

## Meeting Notes

### [26/12/25] - Team Meeting
**Attendees:**
- Enric Talens
- Diego Jimenez
- Sergio Real
- Félix Pridrasanta

**Discussion:**
- Key points discussed
    - Decided on the next moves
    - Correctly naming the needed station parameters
    - Adjusting the global idea of the station

**Decisions:**
- Decisions made
    - There will be a monitor implemented for easing the logic of all the other python nodes
    - We will work with station parameters as no multithreating is permited inside the roboDK enviorment
    - Everyone will be updating it's own README for the rest of the team to read, work will be presented in 2 days from the meeting.

**Action Items:**
- List action items with assignees
  - Sergio will end the placing logic and correct the code for being able to accept and send parameters
  - Diego will end the folding movements and implement the code
  - Felix will develop the first verision of the monitor
  - Enric will implement the conveyor codings
---

## Template for New Entry

```markdown
### [YYYY-MM-DD] - [Brief Description]
**Files Modified:**
- File1
- File2

**Changes Made:**
- Change description

**Reason:**
- Why this change was needed

**Testing:**
- How it was tested

**Results:**
- Outcome of the change

**Notes:**
- Any additional notes
```

---

## Change Statistics

*This section can be updated periodically to track progress*

| Team Member | Entries | Last Update |
|-------------|---------|-------------|
| Enric | 1 | 26/12/25 |
| Sergio | 0 | - |
| Diego | 0 | - |
| Felix | 0 | - |

---

**Last Updated:** December 26, 2025  
**Document Version:** 1.0
