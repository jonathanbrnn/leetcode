class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        res = []

        for num in nums:
            if num in seen:
                res.append(num)
            seen.add(num)

        return res
