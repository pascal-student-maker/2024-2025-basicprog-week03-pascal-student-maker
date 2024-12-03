#11csolution
# Function to check if a year is a leap year
def is_leap_year(year):
    """Returns True if the given year is a leap year, False otherwise."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Get user input for the range of years
start_year = int(input("Enter the start year: "))
end_year = int(input("Enter the end year: "))

# List to store leap years
leap_years = []

# Iterate through the range of years
for year in range(start_year, end_year + 1):
    if is_leap_year(year):
        leap_years.append(year)

# Output the results
if leap_years:
    print(f"The leap years between {start_year} and {end_year} are: {', '.join(map(str, leap_years))}")
else:
    print(f"There are no leap years between {start_year} and {end_year}.")
