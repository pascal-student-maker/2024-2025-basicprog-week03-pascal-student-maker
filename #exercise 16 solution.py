#exercise 16 solution 

import string
import random

# Ask for the minimum and maximum length of the password
x = int(input("Enter the minimum length of the password: "))
y = int(input("Enter the maximum length of the password: "))

# Function to generate a random password
def generate_password_bis(min_length, max_length):
    chosen_length = int(input(f"Choose a password length between {min_length} and {max_length}: "))
    
    # Validate chosen length
    if chosen_length < min_length or chosen_length > max_length:
        print("Invalid length. Please try again.")
        return None
    
    # Generate password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(chosen_length))
    
    return password

# Generate and print the password
password = generate_password_bis(x, y)
if password:
    print(f"Your password is: {password}")
