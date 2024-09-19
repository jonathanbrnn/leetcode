class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indexes = []

        for i, char in enumerate(s):
            if char == c:
                indexes.append(i)

        res = []
        n = len(indexes)

        for i, char in enumerate(s):
            idx = bisect.bisect_left(indexes, i)
            if idx == 0:
                res.append(abs(i - indexes[0]))
            elif idx == n:
                res.append(abs(i - indexes[-1]))
            else:
                before = indexes[idx - 1]
                after = indexes[idx] if idx < n else float("inf")

                res.append(min(abs(i - before), abs(i - after)))

        return res
