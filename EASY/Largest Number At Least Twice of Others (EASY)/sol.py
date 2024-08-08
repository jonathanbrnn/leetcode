class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = nums[0]
        largest_index = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] > largest:
                largest = nums[i]
                largest_index = i
        for i in range(n):
            if nums[i] > largest // 2 and i != largest_index:
                return -1
        return largest_index
