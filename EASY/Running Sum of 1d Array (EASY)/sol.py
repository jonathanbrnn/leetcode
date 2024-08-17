class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        curr = 0

        for num in nums:
            curr += num
            res.append(curr)

        return res
