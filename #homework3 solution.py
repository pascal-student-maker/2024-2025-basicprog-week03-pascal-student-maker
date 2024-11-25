#homework3 solution
# Ask the user for the start and end years
x = int(input("Enter the start year: "))
y = int(input("Enter the end year: "))

# Function to check if a year is a leap year
def is_leap_year(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False

# Loop through the range of years and print the leap years
print("The leap years are:")
leap_years = [i for i in range(x, y + 1) if is_leap_year(i)]
print("The leap years are:", leap_years)
