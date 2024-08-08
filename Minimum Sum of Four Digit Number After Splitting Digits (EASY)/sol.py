class Solution:
    def minimumSum(self, num: int) -> int:
        nums = [x for x in str(num)]
        nums = sorted(nums, key=lambda x: int(x))
        return int(nums[0] + nums[3]) + int(nums[1] + nums[2])
