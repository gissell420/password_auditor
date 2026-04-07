from zxcvbn import zxcvbn

def analyze_password_strength(password):
    result = zxcvbn(password)

    return {
        "score": result["score"],
        "guesses": result["guesses"],
        "crack_times_display": result["crack_times_display"],
        "feedback": result["feedback"]
    }