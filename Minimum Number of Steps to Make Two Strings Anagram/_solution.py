from collections import Counter

s = "anagram"
t = "mangaar"
steps = 0

counter_s = Counter(s)
counter_t = Counter(t)

for char in counter_s:
    if counter_s[char] > counter_t[char]:
        steps += counter_s[char] - counter_t[char]

print(steps)