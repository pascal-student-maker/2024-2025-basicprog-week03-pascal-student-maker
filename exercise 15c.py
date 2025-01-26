howest_email_adress = input("Enter a existing howest-email address: ")

print(howest_email_adress.find('.'))

print(howest_email_adress.find('@'))

firstname = howest_email_adress[0:5]

lastname = howest_email_adress[6:15]



print(f" The firstname is {firstname.capitalize()} and the lastname is {lastname.capitalize()}")

