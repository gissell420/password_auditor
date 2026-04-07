import re

def check_password_policy(password):
    checks = {
        "Minimum 12 characters": len(password) >= 12,
        "Contains uppercase letter": bool(re.search(r"[A-Z]", password)),
        "Contains lowercase letter": bool(re.search(r"[a-z]", password)),
        "Contains digit": bool(re.search(r"\d", password)),
        "Contains special character": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=/\\[\]]", password))
    }

    checks["Overall policy compliant"] = all(checks.values())
    return checks
    