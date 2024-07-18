from collections import Counter

class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        cou = Counter(arr)
        n = len(arr) // 2
        res = 0

        arr = sorted(list(set(arr)), key=lambda x: cou[x])

        while n > 0:
            n -= arr.pop()
            res += 1

        return res


print(Solution().minSetSize([2, 3, 2, 2, 2, 4, 4, 3, 1]))
