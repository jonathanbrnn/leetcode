class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cou = Counter(nums)
        nums = sorted(nums, key=lambda x: (cou[x], -x))
        return nums
