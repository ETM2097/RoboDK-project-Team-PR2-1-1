#!/usr/bin/env python3
"""
Integration Tests for RoboDK Project
Team PR2-1-1

Simple test suite to verify the robot programs and handshake system.
"""

import sys
import time
from threading import Thread

from Handshake.handshake import RobotHandshake
from UR10_PickAndPlace.ur10_config import UR10Config
from UR5_BoxFolding.ur5_config import UR5Config


def test_handshake_basic():
    """Test basic handshake functionality"""
    print("\n[TEST] Testing basic handshake functionality...")
    
    handshake1 = RobotHandshake("UR10")
    handshake2 = RobotHandshake("UR5")
    
    # Test signal sending and receiving
    handshake1.send_signal("UR10", RobotHandshake.SIGNAL_READY)
    result = handshake2.wait_for_signal("UR10", RobotHandshake.SIGNAL_READY, timeout=2)
    
    if result:
        print("[PASS] Basic handshake test passed")
        return True
    else:
        print("[FAIL] Basic handshake test failed")
        return False


def test_ur10_config():
    """Test UR10 configuration"""
    print("\n[TEST] Testing UR10 configuration...")
    
    config = UR10Config()
    
    # Test that positions are defined
    assert config.HOME_POSITION is not None
    assert config.PICK_POSITION is not None
    assert config.PLACE_POSITION is not None
    assert len(config.HOME_POSITION) == 3
    
    print("[PASS] UR10 configuration test passed")
    return True


def test_ur5_config():
    """Test UR5 configuration"""
    print("\n[TEST] Testing UR5 configuration...")
    
    config = UR5Config()
    
    # Test that positions are defined
    assert config.HOME_POSITION is not None
    assert config.CONVEYOR_POSITION is not None
    assert config.FOLDING_SEQUENCE is not None
    assert len(config.FOLDING_SEQUENCE) > 0
    
    print("[PASS] UR5 configuration test passed")
    return True


def test_signal_timeout():
    """Test handshake timeout functionality"""
    print("\n[TEST] Testing handshake timeout...")
    
    handshake = RobotHandshake("TEST")
    
    # This should timeout since no signal is sent
    result = handshake.wait_for_signal("NONEXISTENT", RobotHandshake.SIGNAL_READY, timeout=2)
    
    if not result:
        print("[PASS] Timeout test passed")
        return True
    else:
        print("[FAIL] Timeout test failed")
        return False


def test_signal_types():
    """Test all signal types"""
    print("\n[TEST] Testing all signal types...")
    
    handshake = RobotHandshake("TEST")
    
    # Test all signal types
    signals = [
        RobotHandshake.SIGNAL_READY,
        RobotHandshake.SIGNAL_COMPLETE,
        RobotHandshake.SIGNAL_ERROR,
        RobotHandshake.SIGNAL_WAITING
    ]
    
    for signal in signals:
        handshake.send_signal("TEST", signal)
        result = handshake.get_signal("TEST")
        if result is None or result['signal'] != signal:
            print(f"[FAIL] Signal type test failed for {signal}")
            return False
    
    print("[PASS] All signal types test passed")
    return True


def test_concurrent_operations():
    """Test concurrent robot operations"""
    print("\n[TEST] Testing concurrent operations...")
    
    handshake = RobotHandshake("CONCURRENT")
    handshake.reset_all_signals()
    
    results = {'ur10': False, 'ur5': False}
    
    def ur10_operation():
        h = RobotHandshake("UR10")
        h.send_signal("UR10", RobotHandshake.SIGNAL_READY)
        time.sleep(0.1)
        h.send_signal("UR10", RobotHandshake.SIGNAL_COMPLETE)
        results['ur10'] = True
    
    def ur5_operation():
        h = RobotHandshake("UR5")
        result = h.wait_for_signal("UR10", RobotHandshake.SIGNAL_COMPLETE, timeout=2)
        if result:
            h.send_signal("UR5", RobotHandshake.SIGNAL_READY)
            results['ur5'] = True
    
    # Start both operations
    t1 = Thread(target=ur10_operation)
    t2 = Thread(target=ur5_operation)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    if results['ur10'] and results['ur5']:
        print("[PASS] Concurrent operations test passed")
        return True
    else:
        print("[FAIL] Concurrent operations test failed")
        return False


def run_all_tests():
    """Run all tests"""
    print("="*70)
    print("RoboDK Project Integration Tests")
    print("Team PR2-1-1")
    print("="*70)
    
    tests = [
        ("Basic Handshake", test_handshake_basic),
        ("UR10 Configuration", test_ur10_config),
        ("UR5 Configuration", test_ur5_config),
        ("Signal Timeout", test_signal_timeout),
        ("Signal Types", test_signal_types),
        ("Concurrent Operations", test_concurrent_operations),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"[FAIL] {test_name} raised exception: {e}")
            failed += 1
    
    print("\n" + "="*70)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("="*70)
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
