import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]):
        paragraph = paragraph.lower()
        paragraph = re.findall(r'\b\w+\b', paragraph)
        cou = Counter(paragraph)
        for word, count in cou.most_common():
            if word not in banned:
                return word


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
sol = Solution()
print(sol.mostCommonWord(paragraph, banned))
