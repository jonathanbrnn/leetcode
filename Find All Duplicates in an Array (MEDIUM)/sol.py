from collections import Counter

class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        duplicates = []
        cou = Counter(nums)
        for item, val in cou.items():
            if val == 2:
                duplicates.append(item)
        return duplicates


nums = [4,3,2,7,8,2,3,1]
sol = Solution()
print(sol.findDuplicates(nums))
