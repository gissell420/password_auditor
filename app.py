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
    
def batch(): 
    location = input("Enter the file location: ")
    try:
        password_file = open(location, 'r')
    except FileNotFoundError:
        print("File not found.")
        return
    pass_list = [line.strip() for line in password_file] #clean passwords & store in list
    
    #scorekeeping variables for batch processing
    total_passwords = len(pass_list) #total number of passwords in the batch
    compliant_count = 0 #how many users followed the policy
    leaked_count = 0 #tracks how many passwords were found in data breaches

    i = 1
    print('\n===== COMPLIANCE REPORT =====')
    #loops through each password in the batch and analyzes it 
    for password in pass_list:
        strength_result = analyze_password_strength(password)
        policy_result = check_password_policy(password)
        leaks = int(check_pwned_api(password)) 

        #results tracking for summary
        if policy_result["Overall policy compliant"]: #tracks if user followed policy
            compliant_count += 1
        if leaks > 0: #tracks if password was found in data breaches
            leaked_count += 1
        print(f'{i}:')
        i += 1
        print_report(strength_result, policy_result, leaks, batch=True)
    
    #final summary
    print("\n" + "="*40)
    print("FINAL AUDIT SUMMARY")
    print("="*40)
    print(f"Total Passwords Audited:\t{total_passwords}")
    print(f"Policy Compliant(s):\t\t{compliant_count}")
    print(f"Policy Non-Compliant(s):\t{total_passwords - compliant_count}")
    print(f"Flagged in Data Leaks:\t\t{leaked_count}")
    print("="*40 + "\n")

if __name__ == "__main__":
    main()
