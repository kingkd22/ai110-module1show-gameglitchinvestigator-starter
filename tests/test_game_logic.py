import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic_utils import (
    check_guess, 
    get_range_for_difficulty, 
    parse_guess, 
    update_score,
    initialize_game_state,
    reset_game_state
)


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


# ============================================================================
# get_range_for_difficulty tests
# ============================================================================

def test_range_for_easy_difficulty():
    """Test that Easy difficulty returns range 1-20"""
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20


def test_range_for_normal_difficulty():
    """Test that Normal difficulty returns range 1-100"""
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100


def test_range_for_hard_difficulty():
    """Test that Hard difficulty returns range 1-50"""
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50


def test_range_for_unknown_difficulty():
    """Test that unknown difficulty defaults to Normal range (1-100)"""
    low, high = get_range_for_difficulty("Unknown")
    assert low == 1
    assert high == 100


# ============================================================================
# parse_guess tests
# ============================================================================

def test_parse_guess_valid_integer():
    """Test parsing a valid integer string"""
    ok, value, error = parse_guess("42")
    assert ok is True
    assert value == 42
    assert error is None


def test_parse_guess_valid_float():
    """Test parsing a float string (should convert to int)"""
    ok, value, error = parse_guess("42.7")
    assert ok is True
    assert value == 42
    assert error is None


def test_parse_guess_empty_string():
    """Test parsing an empty string"""
    ok, value, error = parse_guess("")
    assert ok is False
    assert value is None
    assert error == "Enter a guess."


def test_parse_guess_none():
    """Test parsing None value"""
    ok, value, error = parse_guess(None)
    assert ok is False
    assert value is None
    assert error == "Enter a guess."


def test_parse_guess_invalid_text():
    """Test parsing invalid text"""
    ok, value, error = parse_guess("abc")
    assert ok is False
    assert value is None
    assert error == "That is not a number."


def test_parse_guess_negative_number():
    """Test parsing a negative number"""
    ok, value, error = parse_guess("-10")
    assert ok is True
    assert value == -10
    assert error is None


def test_parse_guess_zero():
    """Test parsing zero"""
    ok, value, error = parse_guess("0")
    assert ok is True
    assert value == 0
    assert error is None


# ============================================================================
# update_score tests
# ============================================================================

def test_update_score_win_first_attempt():
    """Test score update for winning on first attempt"""
    score = update_score(0, "Win", 1)
    # 100 - 10 * (1 + 1) = 100 - 20 = 80
    assert score == 80


def test_update_score_win_fifth_attempt():
    """Test score update for winning on fifth attempt"""
    score = update_score(0, "Win", 5)
    # 100 - 10 * (5 + 1) = 100 - 60 = 40
    assert score == 40


def test_update_score_win_minimum_points():
    """Test that winning score never goes below 10 points"""
    score = update_score(0, "Win", 20)
    # 100 - 10 * (20 + 1) = 100 - 210 = -110, but min is 10
    assert score == 10


def test_update_score_too_high_even_attempt():
    """Test score update for Too High on even attempt (adds 5)"""
    score = update_score(50, "Too High", 2)
    # Even attempt: add 5
    assert score == 55


def test_update_score_too_high_odd_attempt():
    """Test score update for Too High on odd attempt (subtracts 5)"""
    score = update_score(50, "Too High", 3)
    # Odd attempt: subtract 5
    assert score == 45


def test_update_score_too_low():
    """Test score update for Too Low (always subtracts 5)"""
    score = update_score(50, "Too Low", 1)
    assert score == 45


def test_update_score_too_low_multiple():
    """Test score update for Too Low from existing score"""
    score = update_score(100, "Too Low", 5)
    assert score == 95


def test_update_score_unknown_outcome():
    """Test that unknown outcome returns current score unchanged"""
    score = update_score(50, "Unknown", 1)
    assert score == 50


def test_update_score_with_existing_score():
    """Test score accumulation over multiple attempts"""
    score = 0
    score = update_score(score, "Too Low", 1)  # 0 - 5 = -5
    score = update_score(score, "Too High", 2)  # -5 + 5 = 0
    score = update_score(score, "Win", 3)  # 0 + (100 - 10*4) = 60
    assert score == 60


# ============================================================================
# New game / game state tests
# ============================================================================

def test_initialize_game_state_easy():
    """Test initializing game state for Easy difficulty"""
    state = initialize_game_state("Easy")
    assert state["attempts"] == 1
    assert state["score"] == 0
    assert state["status"] == "playing"
    assert state["history"] == []


def test_initialize_game_state_normal():
    """Test initializing game state for Normal difficulty"""
    state = initialize_game_state("Normal")
    assert state["attempts"] == 1
    assert state["score"] == 0
    assert state["status"] == "playing"
    assert state["history"] == []


def test_initialize_game_state_hard():
    """Test initializing game state for Hard difficulty"""
    state = initialize_game_state("Hard")
    assert state["attempts"] == 1
    assert state["score"] == 0
    assert state["status"] == "playing"
    assert state["history"] == []


def test_reset_game_state():
    """Test reset_game_state returns fresh state"""
    state = reset_game_state("Normal")
    assert state["attempts"] == 1
    assert state["score"] == 0
    assert state["status"] == "playing"
    assert state["history"] == []


def test_reset_game_state_is_independent():
    """Test that each reset returns a new independent dict"""
    state1 = reset_game_state("Easy")
    state2 = reset_game_state("Hard")
    
    # Modify state1
    state1["attempts"] = 5
    state1["score"] = 100
    state1["history"].append(50)
    
    # state2 should be unaffected
    assert state2["attempts"] == 1
    assert state2["score"] == 0
    assert state2["history"] == []


def test_game_state_structure():
    """Test that game state has all required keys"""
    state = initialize_game_state("Normal")
    required_keys = {"attempts", "score", "status", "history"}
    assert set(state.keys()) == required_keys


def test_game_state_history_is_list():
    """Test that history is initialized as an empty list"""
    state = initialize_game_state("Easy")
    assert isinstance(state["history"], list)
    assert len(state["history"]) == 0


def test_game_state_default_values():
    """Test all default values are correct"""
    state = initialize_game_state("Normal")
    assert isinstance(state["attempts"], int)
    assert isinstance(state["score"], int)
    assert isinstance(state["status"], str)
    assert isinstance(state["history"], list)
    assert state["attempts"] > 0  # Should start at 1, not 0


