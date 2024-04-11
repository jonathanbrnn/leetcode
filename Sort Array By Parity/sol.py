class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        even, odd = [i for i in nums if i % 2 == 0], [i for i in nums if i % 2 != 0]
        even += odd
        return even


print(Solution().sortArrayByParity([1,2,3,4,5,6]))
