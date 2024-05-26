class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(1 for val in set(nums) if val > 0)

# Or Approach 2:
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums) - {0})
