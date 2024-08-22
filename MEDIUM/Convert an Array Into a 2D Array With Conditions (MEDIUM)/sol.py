class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cou = Counter(nums)
        res = []
        n = len(nums)
        nums = set(nums)

        while n > 0:
            curr = []
            for num in nums:
                if cou[num] > 0:
                    curr.append(num)
                    cou[num] -= 1
            res.append(curr)
            n -= len(curr)

        return res
