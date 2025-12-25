"""
RoboDK Project Demonstration Script
Team PR2-1-1

This script demonstrates the coordinated operation of UR10 and UR5 robots
using the handshake communication system.

Run this to see how the robots communicate and work together.
"""

import sys
import time
from threading import Thread

# Import robot programs
from UR10_PickAndPlace.ur10_program import UR10PickAndPlace
from UR5_BoxFolding.ur5_program import UR5BoxFolding
from Handshake.handshake import RobotHandshake, test_handshake


def run_ur10_robot(cycles=1):
    """
    Run UR10 robot for specified number of cycles
    
    Args:
        cycles: Number of pick and place cycles to execute
    """
    robot = UR10PickAndPlace()
    robot.initialize()
    
    for i in range(cycles):
        print(f"\n[DEMO] UR10 Cycle {i+1}/{cycles}")
        robot.run_pick_and_place_cycle()
        time.sleep(1)  # Small delay between cycles


def run_ur5_robot(cycles=1):
    """
    Run UR5 robot for specified number of cycles
    
    Args:
        cycles: Number of folding cycles to execute
    """
    robot = UR5BoxFolding()
    robot.initialize()
    
    for i in range(cycles):
        print(f"\n[DEMO] UR5 Cycle {i+1}/{cycles}")
        robot.run_folding_cycle(box_id=i+1)
        time.sleep(1)  # Small delay between cycles


def demonstrate_synchronized_operation(cycles=2):
    """
    Demonstrate both robots working simultaneously with synchronization
    
    Args:
        cycles: Number of cycles to run
    """
    print("\n" + "="*70)
    print("RoboDK PROJECT DEMONSTRATION")
    print("Team PR2-1-1 - Synchronized Robot Operations")
    print("="*70)
    
    print("\nThis demonstration shows:")
    print("- UR10 performing pick and place operations (Sergio)")
    print("- UR5 performing box folding and conveyor operations (Diego)")
    print("- Handshake communication for synchronization (Felix)")
    
    print(f"\nRunning {cycles} synchronized cycles...\n")
    
    # Reset handshake system
    handshake = RobotHandshake("DEMO")
    handshake.reset_all_signals()
    
    # Create threads for both robots
    ur10_thread = Thread(target=run_ur10_robot, args=(cycles,), name="UR10-Thread")
    ur5_thread = Thread(target=run_ur5_robot, args=(cycles,), name="UR5-Thread")
    
    # Start both robots
    print("[DEMO] Starting both robots...\n")
    ur10_thread.start()
    time.sleep(0.5)  # Small delay to show initialization
    ur5_thread.start()
    
    # Wait for both to complete
    ur10_thread.join()
    ur5_thread.join()
    
    print("\n" + "="*70)
    print("DEMONSTRATION COMPLETE")
    print("="*70)
    print("\nBoth robots completed their operations successfully!")
    print("The handshake system ensured synchronized operation.")
    print("\nNext Steps:")
    print("1. Sergio: Complete UR10 RoboDK integration")
    print("2. Diego: Complete UR5 RoboDK integration")
    print("3. Felix: Review and test handshake system thoroughly")
    print("\nSee Documentation/ folder for detailed information.")
    print("="*70 + "\n")


def main():
    """Main function"""
    print("\nRoboDK Project - Team PR2-1-1")
    print("Choose demonstration mode:")
    print("1. Full synchronized operation (both robots)")
    print("2. UR10 only")
    print("3. UR5 only")
    print("4. Handshake system test")
    
    choice = input("\nEnter your choice (1-4) or press Enter for full demo: ").strip()
    
    if choice == "2":
        print("\nRunning UR10 demonstration...")
        run_ur10_robot(cycles=1)
    elif choice == "3":
        print("\nRunning UR5 demonstration...")
        run_ur5_robot(cycles=1)
    elif choice == "4":
        print("\nRunning handshake system test...")
        test_handshake()
    else:
        # Default: full demonstration
        demonstrate_synchronized_operation(cycles=2)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[DEMO] Demonstration interrupted by user")
        print("Exiting...")
    except Exception as e:
        print(f"\n[DEMO] Error occurred: {e}")
        import traceback
        traceback.print_exc()
