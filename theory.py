list1 = ['pyschics','chemistry','1997','2000']
list2 = [1,2,3,4,5]
list3 = ["a","b","c","d","e"]
list4,list5 = [123,'xyz'],[456,'abc']
print(list1[3])
print(list2[-1])
print(list2[0:2])
list2.append(6)
list2.append(7)
print(list2)
list2.insert(3,55)
print(list2)
list2[3] = 10
print(list2)
list2[6] = 10
del(list2[3])
print(list2)
len([1,2,3])
[1,2,3] + [4,5,6]
['Hi'] * 4
3 in [1,2,3]
list3 = ["a","b","c","d"]
if "c" in list3:
    print("Present")
else:
    print("Not present.")    
print("\nLooping over a list of containing numbers using a for-loop:") 
new_list_numbers = [12,2.6,74,-58,26]   
for number in new_list_numbers:
  print(f"{number}")
list3 = ["a","b","c","d"]
if "c" in list3:
  print("Present!")
else:
    print("Not present")
def calculate_sum(numbers):  # Remove type hints
    total = 0
    for number in numbers:
        total = total + number
    return total

my_favorite_numbers = [10, 14, 58, 36, 1, 5, 12]
print(
    f" Check after function calculate_sum: the total is {calculate_sum(my_favorite_numbers)}"
)
def change_list(list_numbers:list[int]) -> None:
    list_numbers.append(100)
    list_numbers.append(500)
print("\nA list can also be used as a parameter.")   
my_favorite_numbers = [10,14,58,36,1,5,12] 
print(f"Orginallist: {my_favorite_numbers}")
change_list(my_favorite_numbers)
print(f"Check after function change_list: {my_favorite_numbers}")

import random  # Import the random module

def return_random_list(amount: int) -> list[int]:
    result = []
    for index in range(0, amount):
        result.append(random.randrange(0, 10))  # Generate a random number between 0 and 9
    return result

# Generate a random list of 20 numbers and print it
print(f"A random list for checking for doubles:\n{return_random_list(20)}")
