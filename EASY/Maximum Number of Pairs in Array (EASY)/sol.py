class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cou = Counter(nums)
        pairs = 0
        leftovers = 0

        for val in cou.values():
            pairs += val // 2
            if val % 2 != 0:
                leftovers += 1

        return [pairs, leftovers]
