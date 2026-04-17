from strength import analyze_password_strength
from policy import check_password_policy
from report import print_report
from pwned_api import check_pwned_api

def main():
    print("Password Strength Analyzer & Policy Auditor")
    print("------------------------------------------")
    while True:
        print("Options: Single (1) | Batch (2) | Exit (0)")
        try:
            option = int(input("Choice: "))
            match option:
                case 1:
                    single()
                case 2:
                    batch()
                case _:
                    break

        except ValueError:
            print("Enter only the number for an option.")
    print("END") #Remove in final
        


def single():
    password = input("Enter a password to analyze: ")

    strength_result = analyze_password_strength(password)
    policy_result = check_password_policy(password)
    leaks = check_pwned_api(password)

    print_report(strength_result, policy_result, leaks)

        
def batch(): #Can only use zxcvbn on plaintext passwords. Can only use JtR on hashed passwords.
    location = input("Enter the file location:")
    try:
        password_file = open(location,'r')
    except FileNotFoundError:
        print("File not found.")
        return
    pass_list = [line.strip() for line in password_file]
    i = 1;print('\n===== COMPLIANCE REPORT =====')
    for password in pass_list:
        strength_result = analyze_password_strength(password)
        policy_result = check_password_policy(password)
        leaks = check_pwned_api(password)
        print(f'{i}:')
        i+=1
        #Possibly output to txt file in future.
        print_report(strength_result,policy_result,leaks,batch=True)
        


if __name__ == "__main__":
    main()
