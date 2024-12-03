#EXERCISE11.C

a = int(input("Enter the start year"))
b = int(input("Enter the end year"))

def is_leap_year(year):
    """Determine whether a year is a leap year."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
is_leap_year

for i in range(1993,1997):
    total = is_leap_year
print(f" The leap years are> The leap years are : {is_leap_year}") 
   