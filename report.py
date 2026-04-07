def print_report(strength_result, policy_result):
    print("\n===== PASSWORD ANALYSIS REPORT =====")
    print(f"Strength Score: {strength_result['score']} / 4")
    print(f"Estimated Guesses: {strength_result['guesses']}")

    print("\nCrack Time Estimates:")
    for attack_type, estimate in strength_result["crack_times_display"].items():
        print(f"- {attack_type}: {estimate}")

    print("\nPolicy Checks:")
    for check, passed in policy_result.items():
        status = "PASS" if passed else "FAIL"
        print(f"- {check}: {status}")

    feedback = strength_result.get("feedback", {})
    warning = feedback.get("warning")
    suggestions = feedback.get("suggestions", [])

    if warning or suggestions:
        print("\nFeedback:")
        if warning:
            print(f"- Warning: {warning}")
        for suggestion in suggestions:
            print(f"- Suggestion: {suggestion}")

            