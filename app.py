from strength import analyze_password_strength
from policy import check_password_policy
from report import print_report
from pwned_api import check_pwned_api

def main():
    print("Password Strength Analyzer & Policy Auditor")
    print("------------------------------------------")

    password = input("Enter a password to analyze: ")

    strength_result = analyze_password_strength(password)
    policy_result = check_password_policy(password)

    leaks = check_pwned_api(password)

    print_report(strength_result, policy_result, leaks)

if __name__ == "__main__":
    main()