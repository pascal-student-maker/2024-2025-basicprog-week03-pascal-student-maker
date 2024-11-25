#exercise7 solution
# Ask for user input
x = int(input("Enter a start value: "))
step_size = int(input("Enter a positive step size: "))
numbers_printed = int(input("How many numbers need to be printed? "))

# Function to print the desired sequence
def print_list_numbers(start, step, count):
    print("The numbers you are looking for are:")
    for i in range(count):
        print(start + i * step)

# Call the function with the user-provided values
print_list_numbers(x, step_size, numbers_printed)
