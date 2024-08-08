class Solution:
    def sortArrayByParityII(self, nums: list[int]):
        even,odd=[num for num in nums if num%2 != 0 ],[num for num in nums if num%2 == 0]
        result = []
        for x, y in zip(odd, even):
            result.extend([x, y])
        return result


nums = [4,2,7,5]
print(Solution().sortArrayByParityII(nums))
