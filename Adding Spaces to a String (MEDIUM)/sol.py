class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        prev_index = 0

        for index in spaces:
            res.append(s[prev_index:index])
            res.append(" ")
            prev_index = index

        res.append(s[prev_index:])

        return "".join(res)


print(Solution().addSpaces("EnjoyYourCoffee", [5, 9]))
