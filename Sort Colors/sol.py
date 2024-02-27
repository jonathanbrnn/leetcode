# IN ONE LINE BUT IT IS REALLY SLOW:
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        nums = nums.sort()
        return None

# MORE LINES BUT WAY FASTER (BEATS 95% OF USERS):
    class Solution:
        def sortColors(self, nums: list) -> None:
            sol = [0] * (3)
            for num in nums:
                sol[num] += 1
            sol = [0] * (sol[0]) + [1] * (sol[1]) + [2] * (sol[2])
            for i in range(len(nums)):
                nums[i] = sol[i]
