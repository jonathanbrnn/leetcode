class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        curr = []
        last = ""

        for i in range(len(s)):
            if last == "":
                last = s[i]
                curr.append(i)
            elif last != "" and s[i] != last:
                curr.append(i-1)
                if abs(curr[0] - curr[1]) >= 2:
                    res.append(curr)
                last = s[i]
                curr = []
                curr.append(i)
            if i == len(s) - 1:
                curr.append(i)

        if len(curr) > 1:
            if abs(curr[0] - curr[1]) >= 2:
                    res.append(curr)

        return res
