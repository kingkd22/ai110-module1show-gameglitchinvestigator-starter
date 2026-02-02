import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic_utils import check_guess


# Winning guess tests
def test_winning_guess_exact_match():
    """Test that guessing the exact secret number results in a win"""
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_winning_guess_low_number():
    """Test winning with a low secret number"""
    outcome, message = check_guess(5, 5)
    assert outcome == "Win"
    assert "Correct" in message


def test_winning_guess_high_number():
    """Test winning with a high secret number"""
    outcome, message = check_guess(99, 99)
    assert outcome == "Win"
    assert "Correct" in message


# Too high guess tests
def test_guess_too_high_by_one():
    """Test guess that is one higher than secret"""
    outcome, message = check_guess(51, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_high_by_ten():
    """Test guess that is significantly higher than secret"""
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_high_large_difference():
    """Test guess that is much higher than secret"""
    outcome, message = check_guess(100, 25)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_high_at_boundary():
    """Test guess at upper boundary"""
    outcome, message = check_guess(100, 1)
    assert outcome == "Too High"
    assert "LOWER" in message


# Too low guess tests
def test_guess_too_low_by_one():
    """Test guess that is one lower than secret"""
    outcome, message = check_guess(49, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_guess_too_low_by_ten():
    """Test guess that is significantly lower than secret"""
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_guess_too_low_large_difference():
    """Test guess that is much lower than secret"""
    outcome, message = check_guess(10, 90)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_guess_too_low_at_boundary():
    """Test guess at lower boundary"""
    outcome, message = check_guess(1, 100)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# Edge case tests
def test_string_secret_int_guess():
    """Test handling when secret is string and guess is int"""
    outcome, message = check_guess(50, "50")
    assert outcome == "Win"
    assert "Correct" in message


def test_string_secret_guess_too_high():
    """Test string secret with guess too high"""
    outcome, message = check_guess(60, "50")
    assert outcome == "Too High"
    assert "LOWER" in message


def test_string_secret_guess_too_low():
    """Test string secret with guess too low"""
    outcome, message = check_guess(40, "50")
    assert outcome == "Too Low"
    assert "HIGHER" in message
