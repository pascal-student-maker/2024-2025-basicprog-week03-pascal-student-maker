#homework 1 

# Ask the user for a word
word1 = input(str("Enter a word: "))
# Program: Count number of vowels in a String in Python

# example string


vowels = ["a", "e", "i", "o", "u"]
count = 0

# using for-each loop, character is reference to a letter in the string
for character in word1:
    if character in vowels:
        count += 1


print("Number of vowels in the given string is: ", count)

string = word1
vowels = len([char for char in string if char.lower() in {'a', 'e', 'i', 'o', 'u'}])
consonants = len([char for char in string if char.isalpha() and char.lower() not in {'a', 'e', 'i', 'o', 'u'}])
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)