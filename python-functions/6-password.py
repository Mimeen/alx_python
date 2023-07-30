def validate_password(password):
    if len(password) < 8:
        return False
    
    #check for upper, lower cases and digits
    contains_digit = False
    contains_upper = False
    contains_digit = False
    
    for char in password:
        if char.isdigit():
            contains_digit = True
        elif char.isupper():
            contains_upper = True
        elif char.islower():
            contains_lower = True
  
    if not (contains_digit and contains_lower and contains_upper):
        return False   
    
    #check for spaces       
    if ' ' in password:
        return False
    
    return True

# print(validate_password("Password123"))
# print(validate_password("abc123"))
# print(validate_password("Password 123"))
# print(validate_password("password123"))