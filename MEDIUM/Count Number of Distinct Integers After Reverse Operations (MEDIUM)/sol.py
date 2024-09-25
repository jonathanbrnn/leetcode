class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        res = set(nums)

        for num in nums:
            num = int(str(num)[::-1])
            res.add(num)

        return len(res)
