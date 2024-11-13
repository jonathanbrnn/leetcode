class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []

        for a, b in zip(nums, index):
            target.insert(b, a)

        return target
