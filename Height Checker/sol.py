class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = sum([height != exp for height, exp in zip(heights, expected)])
        return count
