class Solution:
    def countElements(self, nums: List[int]) -> int:
        res = 0
        min_nums = min(nums)
        max_nums = max(nums)

        for num in nums:
            if min_nums < num < max_nums:
                res += 1

        return res
