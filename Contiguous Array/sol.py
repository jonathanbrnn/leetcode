class Solution:
    def findMaxLength(self, nums) -> int:
        zero_count = 0
        one_count = 0
        max_length = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            else:
                one_count += 1
            if zero_count == one_count:
                max_length = zero_count + one_count
        return max_length


print(Solution().findMaxLength([0,0,1,0,0,0,1,1]))
