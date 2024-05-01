from collections import Counter

class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        cou1 = Counter(words1)
        cou2 = Counter(words2)
        res = 0
        if len(words1) > len(words2):
            for item, val in cou1.items():
                if val == 1 and cou2[item] == 1:
                    print(item, val, cou2[item])
                    res += 1
        else:
            for item, val in cou2.items():
                if val == 1 and cou1[item] == 1:
                    res += 1
        return res


words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]

print(Solution().countWords(words1, words2))
