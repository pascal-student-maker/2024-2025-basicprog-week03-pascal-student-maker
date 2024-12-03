# Initializing list
test_list = ['abc','xyz']

# printing original lists
print("The original list is : " + str(test_list))

# Swap elements in String list
# using replace() + list comprehension
res = [sub.replace('a', 'x').replace('b', 'y').replace('z', 'c') for sub in test_list]
res1 = [sub.replace('x', 'a').replace('y', 'b').replace('c', 'z') for sub in test_list]

# printing result 

print ("List after performing character swaps : " + str(res) + str(res1))


