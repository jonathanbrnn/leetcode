class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        if target not in set(nums):
            return []

        nums.sort()

        return [i for i, num in enumerate(nums) if num == target]
