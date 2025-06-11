import re

def is_valid_password(password):
    # Check length
    if len(password) < 8:
        return False
    
    # Check for at least one lowercase, one uppercase, and one digit
    has_lower = re.search(r'[a-z]', password)
    has_upper = re.search(r'[A-Z]', password)
    has_digit = re.search(r'[0-9]', password)
    
    return bool(has_lower and has_upper and has_digit)
password = input("Enter password: ")
if is_valid_password(password):
    print("Valid password ")
else:
    print("Invalid password ")
