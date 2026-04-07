from strength import analyze_password_strength
from policy import check_password_policy
from report import print_report

def main():
    print("Password Strength Analyzer & Policy Auditor")
    print("------------------------------------------")

    password = input("Enter a password to analyze: ")

    strength_result = analyze_password_strength(password)
    policy_result = check_password_policy(password)

    print_report(strength_result, policy_result)

if __name__ == "__main__":
    main()