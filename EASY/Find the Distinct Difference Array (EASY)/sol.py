class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        left_seen = set()
        right_seen = set()

        n = len(nums)

        left_count = [0 for i in range(n)]
        right_count = [0 for i in range(n)]

        for i in range(n):
            left_seen.add(nums[i])
            left_count[i] = len(left_seen)

        for i in range(n - 1, -1, -1):
            right_count[i] = len(right_seen)
            right_seen.add(nums[i])

        return [left_count[i] - right_count[i] for i in range(n)]
