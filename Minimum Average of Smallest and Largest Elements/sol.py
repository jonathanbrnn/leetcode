'''
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = float('inf')
        nums.sort()

        for i in range(len(nums) // 2):
            averages = min(averages, (nums.pop() + nums.pop(0)) / 2)

        return averages
'''
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        nums.sort()
        j = -1

        for i in range(len(nums) // 2):
            averages.append((nums[i] + nums[j]) / 2)
            j -= 1

        return min(averages)
