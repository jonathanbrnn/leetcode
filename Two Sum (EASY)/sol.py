class Solution(object):
    def twoSum(self, nums, target):
        left = 0
        right = len(nums) - 1
        check = nums.copy()
        nums.sort()
        while left < right:
            if nums[left] + nums[right] == target:
                a = check.index(nums[left])
                check[a] = None  # Mark the element as None instead of removing it
                b = check.index(nums[right])
                return a, b
            if nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1

print(Solution().twoSum([3,3], 6))