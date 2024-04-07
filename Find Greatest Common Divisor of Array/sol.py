class Solution:
    def findGCD(self, nums: list[int]):
        minNum = min(nums)
        maxNum = max(nums)
        greatest = 0
        for i in range(1, minNum + 1):
            if minNum % i == 0 and maxNum % i == 0:
                greatest = i
        return greatest


nums = [2,7,5,6,8,3,10]
print(Solution().findGCD(nums))
