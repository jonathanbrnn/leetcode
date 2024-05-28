class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        if n == 1:
            return nums[0]

        prev_max = nums[0]
        curr_max = max(nums[0], nums[1])

        for i in range(2, n):
            new_max = max(prev_max + nums[i], curr_max)
            prev_max, curr_max = curr_max, new_max

        return curr_max
