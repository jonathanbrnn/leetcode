# Python is way too powerful.

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        for i in range(1, n + 1):
            res.append(i)

        res.sort(key=str)

        return res
