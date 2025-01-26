import random 

Attempts = 1

number = int(input("Enter a number:"))
correct_number = random.randint(0,20)


while number != correct_number:
    print("Error try again")
    
    if number >  correct_number:
        print("  Number is too big")
        
    elif number < correct_number:
        print(" number is too small")   
    
    number = int(input("Enter a number:"))
 
    Attempts += 1
print(f" Congratulatons you guessed the right number: in only {Attempts} tries.")   


 
        
         

