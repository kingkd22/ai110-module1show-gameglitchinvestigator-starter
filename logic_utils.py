def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # Convert both to int for proper comparison
    try:
        guess_int = int(guess)
        secret_int = int(secret)
    except (ValueError, TypeError):
        return "Error", "Invalid comparison"
    
    if guess_int == secret_int:
        return "Win", "🎉 Correct!"
    elif guess_int > secret_int:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


def initialize_game_state(difficulty: str):
    """
    Initialize a new game state with default values.
    
    Returns: dict with keys: attempts, score, status, history
    """
    return {
        "attempts": 1,
        "score": 0,
        "status": "playing",
        "history": []
    }


def reset_game_state(difficulty: str):
    """
    Reset game state for a new game.
    Alias for initialize_game_state for clarity.
    
    Returns: dict with keys: attempts, score, status, history
    """
    return initialize_game_state(difficulty)
