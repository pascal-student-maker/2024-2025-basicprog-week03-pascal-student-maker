#homework4 
import re  
  
def validate_email(email):  
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):  
        return True  
    return False  
  
email = "pascal.musabyimana@student.howest.be"  
if validate_email(email):  
    print("Valid email address")  
else:  
    print("Invalid email address")