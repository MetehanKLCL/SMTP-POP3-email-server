import re

def validate_password(password):
    '''
    Password should contains at least 8 characters
    At least 1 lowercase
    At least 1 uppercase
    at least 1 special character
    '''

    if len(password) < 8:
        return "Password must be at least 8 characters long"
    
    if not any(char.islower() for char in password):
        return "Password must contain at least 1 lowercase letter"
    
    if not any(char.isupper() for char in password):
        return "Password must contain at least 1 uppercase letter"
    
    if not re.search(r"[^a-zA-Z0-9]", password):
        return "Password must contain at least 1 special character (., !, @, - etc.)"