def password(lastname:str,firstname:str,birthday:int):
    letter = lastname[0:3].lower() 
    secondletter = firstname[0:2].upper()
    birthdayletter = birthday[3:5] 
    lastletterbirthday = birthday[8:10]
    
    combination = letter + secondletter + birthdayletter + lastletterbirthday
    print(combination)
    
lastname = input("Enter your last name: ") 
firstname = input("Enter your first name: ")  
birthday = input("Enter your date of birth (dd-mm-yyyy):") 

password(lastname,firstname,birthday)
