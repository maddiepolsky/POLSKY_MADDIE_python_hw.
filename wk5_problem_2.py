#A website requires the users to input username and password to register. Write a function to check the validity of password input by users.
# Following are the criteria for checking the password: 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6 
# 5. Maximum length of transaction password: 12
import re
def check_password(password):
    if len(password)< 6:
        return "Invalid Password: Password must be longer than 6 characters."
    if len(password) > 12:
        return "Invalid Password: Password cannot be longer than 12 characters."
    if not re.search("[a-z']", password):
        return "Invalid Password: Should contain at least one lowercase letter."
    if not re.search("[A-Z]", password):
        return "Invalid Password: Should contain at least one upper case letter."
    if not re.search("[0-9]", password):
        return "Invalid Password: Should contain at least one number."
    if not re.search("[$#@]", password):
        return "Invalid password: Should contain at least one special character: $, #, or @."
    return "Valid Password"

password = "Aa$@12x"
print (check_password(password))