class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = (float('inf'), 0)

        for num in nums:
            if abs(num) < res[0]:
                res = (abs(num), num)

        if abs(res[1]) in nums:
            return abs(res[1])
        else:
            return res[1]
