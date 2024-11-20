# This solution isn't great, but it now actually complies with the problem statement's requirements (the previous solution used the built-in sorting function :/).
class Solution:
    def sortColors(self, nums: list) -> None:
        count = [0, 0, 0]

        for num in nums:
            count[num] += 1

        sol = [0] * count[0] + [1] * count[1] + [2] * count[2]

        for i in range(len(nums)):
            nums[i] = sol[i]

        return nums
