class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cou = Counter(nums)
        highest = 0
        occ = 0
        for val in cou.values():
            if val > highest:
                highest = val
                occ = 1
            elif val == highest:
                occ += 1
        return occ * highest
