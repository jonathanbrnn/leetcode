class Solution:
    def clearDigits(self, s: str) -> str:
        to_skip = []
        n = len(s)
        res = ""

        for i in range(n):
            if s[i].isdigit():
                to_skip.append(i)
                for j in range(i, -1, -1):
                    if s[j].isdigit() == False and j not in to_skip:
                        to_skip.append(j)
                        break

        if to_skip == []:
            return s

        for i in range(n):
            if i not in to_skip:
                res += s[i]

        return res
