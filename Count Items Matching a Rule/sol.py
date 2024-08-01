class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        s = 0
        res = 0

        if ruleKey == "color":
            s = 1
        if ruleKey == "name":
            s = 2

        for i in range(len(items)):
            if items[i][s] == ruleValue:
                res += 1

        return res
