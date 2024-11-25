#homework2  solution
# Ask the user for input
word1 = input("Enter a word: ")

# Define the vowels
vowels_set = {"a", "e", "i", "o", "u"}

# Count vowels and consonants
vowels = len([char for char in word1 if char.lower() in vowels_set])
consonants = len([char for char in word1 if char.isalpha() and char.lower() not in vowels_set])

# Remove vowels from the string
result = ''.join([char for char in word1 if char.lower() not in vowels_set])

# Print the results
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
print("String after removing vowels:", result)
