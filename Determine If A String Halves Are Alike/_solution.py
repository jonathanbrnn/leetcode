s = 'book'
halfpoint = int(len(s) / 2)
a = s[:halfpoint]

vowels = 0
for char in s:
    if char in 'aeiouAEIOU':
        vowels += 1
bVowels = 0
for char in a:
    if char in 'aeiouAEIOU':
        bVowels += 1

print((vowels / 2) == bVowels)