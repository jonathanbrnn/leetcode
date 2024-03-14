class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = {0: 1}
        current = 0
        total_subarrays = 0

        for num in nums:
            current += num
            if current - goal in count:
                total_subarrays += count[current - goal]
            count[current] = count.get(current, 0) + 1

        return total_subarrays


nums = [1,0,1,0,1]
goal = 2
sol = Solution()
print(sol.numSubarraysWithSum(nums, goal))
