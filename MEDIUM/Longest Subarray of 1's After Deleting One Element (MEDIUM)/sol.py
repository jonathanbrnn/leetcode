class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        curr_ones = 0
        prev_ones = 0
        curr_zeros = 0
        res = 0
        n = len(nums)

        if n == nums.count(1):
            return n - 1

        for i in range(n):
            if nums[i] == 1:
                curr_ones += 1
            elif nums[i] == 0 and curr_zeros == 0:
                curr_zeros += 1
                prev_ones = curr_ones
                curr_ones = 0
            elif nums[i] == 0 and curr_zeros == 1:
                res = max(res, curr_ones + prev_ones)
                prev_ones = curr_ones
                curr_ones = 0
        res = max(res, curr_ones + prev_ones)

        return res


print(Solution().longestSubarray([1,1,1]))
