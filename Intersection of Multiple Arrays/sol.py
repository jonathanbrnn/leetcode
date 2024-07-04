class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = set(nums[0])
        for num in nums:
            res = set.intersection(res, set(num))

        return sorted(list(res))
