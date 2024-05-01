# 01.05.2024 - 09:24
# First Attempt, submitted originally on April 26th [34ms, 16.47mb] -> beats 97.57% and 93.22% of users
# Then resubmitted on May 1st [34ms, 16.29mb] -> beats 63.06% and 100% of users
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, char in enumerate(word):
            if char == ch:
                word = (word[:i+1])[::-1] + word[i+1:]
                break
        return word


# Further optimised Solution, submitted on May 1st [24ms, 16.31mb] -> beats 98.22% and 94.56% of users
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                return (word[:i+1])[::-1] + word[i+1:]
        return word


# What do I learn from this? Leetcodes profiler is utter garbage and does not accurately reflect your codes runtime!
# Neither Solution is really different from the other. They both use the same core logic, but get vastly
# different runtimes as of today.
# I'm sure in a few hours the other submissions will be way better than mine. The next time
# (if there is ever going to be a 'next time' for this solution) my submission will probably only beat 40 - 50%.
