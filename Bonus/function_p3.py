# Function to validate password

def Strong_Password(password):

    # Rule 1: Length > = 8
    if len(password) < 8:
        return f"Weak Password"

    # Rule 2: At least one uppercase letter
    if not any(char.isupper() for char in password):
        return f"Weak Password"
    # Rule 3: At least one digit

    if not any(char.isdigit() for char in password):
        return f"Weak Password"
    return f"Strong Password"

print(Strong_Password("Password1233"))


