class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        res = ""
        i = 0
        while i < len(num):
            while k > 0 and res and res[-1] > num[i]:
                res = res[:-1]
                k -= 1
            res += num[i]
            i += 1
        while k > 0:
            res = res[:-1]
            k -= 1
        res = res.lstrip('0')
        return "0" if not res else res


print(Solution().removeKdigits("1111111", 3))
