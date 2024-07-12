# First Attempt, [34ms, 16.63mb]
class Solution:
    def printVertically(self, s: str) -> List[str]:
        max_length = 0
        s = s.split(" ")

        for word in s:
            max_length = max(max_length, len(word))

        res = [""] * max_length

        for word in s:
            n = len(word)
            for i in range(max_length):
                if i < n:
                    res[i] += word[i]
                else:
                    res[i] += " "

        res = [x.rstrip() for x in res]

        return res

# Improved Runtime, [27ms, 16.52mb]
class Solution:
    def printVertically(self, s: str) -> List[str]:
        max_length = 0
        s = s.split(" ")

        for word in s:
            max_length = max(max_length, len(word))

        res = []

        for i in range(max_length):
            curr = ""
            for word in s:
                n = len(word)
                if i < n:
                    curr += word[i]
                else:
                    curr += " "

            res.append(curr.rstrip())

        return res
