def check_emailadress( firstname:str ,lastname:str , emailadress:str) -> str:
     return firstname  + "" + lastname  + "" + emailadress
result = check_emailadress("pascal","musabyimana","@student.howest.be")
print(result)
if result ==  check_emailadress("pascal","musabyimana","@student.howest.be"):
    print(" Valid emailadress")
else: print(" Not a valid email adress")
    





