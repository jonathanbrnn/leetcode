from gentest import GenerateTestCases

newGen = GenerateTestCases()
nums = newGen.genNums(-10000, 10000, 10000000)
target = newGen.genTarget(-10000, 10000)
newGen.writeToFile("testcases.txt", nums, target)

with open("testcases.txt", "r") as f:
    x = f.readlines()
    target = int(x[1])
    print(target)
    nums = list(map(int, x[0].split()))


class Solution:
    def twoSum(self, nums: list[int], target: int):
        for num in nums:
            for other in nums:
                if num + other == target:
                    return num, other

    def twoSum2(self, nums, target):
        left = 0
        right = len(nums)-1
        nums.sort()
        while left < right:
            if nums[left] + nums[right] == target:
                return nums[left], nums[right]
                break
            if nums[left] + nums[right] < target:
                left+=1
            else:
                right-=1
        return "None found!"

newSol = Solution()
print(newSol.twoSum2(nums, target))
print(newSol.twoSum(nums, target))
