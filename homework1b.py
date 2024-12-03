#homework1b.py
word = "apple"
vowel_count = 0

for char in word:
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        vowel_count += 1

print("Number of vowels:", vowel_count)

word = "apple"
consant_count = 0
for char in word:
    if char.lower() in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']:
        consant_count += 1
print(" Number of consant:",consant_count)    
    