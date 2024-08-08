class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == target:
                return [left + 1, right + 1]
            if nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
