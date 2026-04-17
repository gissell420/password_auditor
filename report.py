def print_report(strength_result, policy_result, leaks, batch: bool = False):
    if not batch: #Single
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

        print("\nData Breach Check:")
        if int(leaks) > 0:
            print(f"❌ CAUTION: This password was seen in {leaks} data leaks!")
            print("Suggestion: Change this password immediately on all accounts.")
        else:
            print("✅ Safe! This password has not been found in known breaches.")

        feedback = strength_result.get("feedback", {})
        warning = feedback.get("warning")
        suggestions = feedback.get("suggestions", [])

        if warning or suggestions:
            print("\nFeedback:")
            if warning:
                print(f"- Warning: {warning}")
            for suggestion in suggestions:
                print(f"- Suggestion: {suggestion}")


    else: #Batch (Removes headers and adds tabs to front. 
            #Can probably integrate into the prior stuff with more conditionals/ternary but opted not to.)
        print(f"\tStrength Score: {strength_result['score']} / 4")
        print(f"\tEstimated Guesses: {strength_result['guesses']}")
        for attack_type, estimate in strength_result["crack_times_display"].items():
            print(f"\t- {attack_type}: {estimate}")
        print(f'\tOverall Policy Compliance: {policy_result["Overall policy compliant"]}')
        if int(leaks) > 0:
            print(f"\t❌ CAUTION: This password was seen in {leaks} data leaks!")
            print("\tSuggestion: Change this password immediately on all accounts.")
        else:
            print("\t✅ Safe! This password has not been found in known breaches.")

