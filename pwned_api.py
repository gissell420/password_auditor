import requests
import hashlib

def check_pwned_api(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1_password[:5], sha1_password[5:]

    url = f'https://api.pwnedpasswords.com/range/{first5}'
    response = requests.get(url)

    if response.status_code == 200:
        hashes = (line.split(':') for line in response.text.splitlines())
        for h, count in hashes:
            if h == tail:
                return count
    
    return 0 

# test_password = "password123"
# count = check_pwned_api(test_password)
# print(f"\n[API TEST] The password '{test_password}' was found in {count} data breaches!")