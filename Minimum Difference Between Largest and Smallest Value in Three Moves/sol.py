from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()
        n = len(nums)

        res = []
        res.append(nums[n-4] - nums[0])
        res.append(nums[n-3] - nums[1])
        res.append(nums[n-2] - nums[2])
        res.append(nums[n-1] - nums[3])

        return min(res)



print(Solution().minDifference([6,6,0,1,1,4,6]))
