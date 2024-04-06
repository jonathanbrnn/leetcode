class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        length = len(nums)
        nums = set(nums)
        for i in range(1, length + 1):
            if i not in nums:
                res.append(i)
        return res
