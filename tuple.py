tuple1 = ("a","b","c")

tuple2 = (14,25,85,"test")
print("\n check if an element can be found in tuple 2:")
if 25 in tuple2:
    print("present in tuple2") 
else:
    print(" Not present in tuple2")            
    
tuple3 = tuple1 + tuple2
tuple4 = tuple1 * 4
tuple5 = tuple2[1:3]    
element_from_tumple = tuple2[0]
print(tuple5)
print(len(tuple2))
tuple1 = ("a","b","c")
for letter in tuple1:
    print(letter)
index = 0
while (index < len(tuple1)):
    print(tuple1[index])
    index += 1 
       
# Initial list of courses
list_courses = ["Basic Programming", "Data Science", "Prototyping"]
print(f"\nList courses: {list_courses}")

# Converting list to tuple
tuple_courses = tuple(list_courses)
print(f"Tuple courses: {tuple_courses}")

# Method 1: Convert tuple to list, modify, and convert back to tuple
temp_list = list(tuple_courses)  # Convert tuple to list
temp_list.append("User 1")       # Add a new item
tuple_courses = tuple(temp_list) # Convert back to tuple
print(f"Updated Tuple courses (Method 1): {tuple_courses}")

# Resetting the tuple for demonstration
tuple_courses = tuple(list_courses)

# Method 2: Create a new tuple by concatenation
tuple_courses = tuple_courses + ("User 1",)  # Concatenate a new tuple
print(f"Updated Tuple courses (Method 2): {tuple_courses}")

from typing import Tuple
def calculate_product(elements: Tuple[int]):
    result =1
    for number in elements:
        result += number
    return result 
students = [('Stijn','20','90'),
           ('Johan','17','91'),
           ('Lies','17','93'),
           ('Henk','21','85'),
           ('Tom','19','80')]
for studentinfo in students:
    print(
        f"Name: {studentinfo[0]}, Age: {studentinfo[1]}, Score:{studentinfo[2]}")
    