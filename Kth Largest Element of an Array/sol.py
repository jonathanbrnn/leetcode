import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(len(nums) - k + 1):
            result = heapq.heappop(nums)
        return result


nums = []
k = 1
print(Solution().findKthLargest(nums, k))
