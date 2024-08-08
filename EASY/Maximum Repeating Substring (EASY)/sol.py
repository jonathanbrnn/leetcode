class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if word not in sequence:
            return 0
        res = 0
        x = word
        while True:
            if word in sequence:
                res += 1
                word = word + x
                print(word)
            else:
                return res
                break
