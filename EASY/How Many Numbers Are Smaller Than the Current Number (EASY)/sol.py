class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = sorted(nums)
        res = []
        for num in nums:
            res.append(n.index(num))
        return res
