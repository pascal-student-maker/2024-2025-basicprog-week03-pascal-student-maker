#exercise 11 
x = int(input("enter the start year:"))
y = int(input("enter the end year"))
def is_leap_year(startyear,endyear,n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False
for i in range(x,y):
        print(" is a leap year")
is_leap_year(startyear, endyear,n)       
 