class Solution:
    def areNumbersAscending(self, s) -> bool:
        res = [int(i) for i in s.split() if i.isdigit()]
        return res == sorted(res) and len(res) == len(set(res))





print(Solution().areNumbersAscending("4 5 11 26"))
