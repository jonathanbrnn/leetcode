from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cou = Counter(nums)
        for val, count in cou.items():
            if count == 1:
                return val
