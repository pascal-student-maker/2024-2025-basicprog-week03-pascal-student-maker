import string
import random
def  generate_password_bis(minumum_length:int,maximum_length:int):
    random_source = string.ascii_letters + string.digits + string.punctuation
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    
    for _ in range(minumum_length,maximum_length):
        password += random.choice(random_source)
        
        password_list = list(password)
        
        random.SystemRandom().shuffle(password_list)
        password = ''.join(password_list)
        return password
    
minimum_length = int(input('Enter the mininum length of the password:')) 
maximum_length = int(input("Enter the maximum length of the password:")) 


print(" Your password is: ",generate_password_bis(minimum_length,maximum_length))


        