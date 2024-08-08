from collections import Counter

class Solution:
    def findDuplicate(self, nums: list[int]):
        cou = Counter(nums)
        for item, val in cou.items():
            if val >= 2:
                return item

nums = [1,3,3,4,5,2]
sol = Solution()
print(sol.findDuplicate(nums))
