#exercise16c
import random
import string

input("Enter the minimum length of the password:")
input("Enter the maximum length of the password:")

def generate_password_bis():
    length = random.randint(5, 10)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print(f" Your password is : {generate_password_bis()}")