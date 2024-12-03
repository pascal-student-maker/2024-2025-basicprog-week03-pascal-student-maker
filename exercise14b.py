#exercise14b
import datetime
format = "%d/%m/%Y"

a = input(" Enter your last name:")
b = input("Enter your first name:")
c = input("Enter your date of birth (dd/mm/yyyy): ")

letter = a[0:3]
print(letter.lower())

letter1 = b[0:2]
print(letter1.upper())

letter2 = c[0:5]
print(letter2)

together = letter.lower() + ""  + letter1.upper() + "" + letter2
print(together)


