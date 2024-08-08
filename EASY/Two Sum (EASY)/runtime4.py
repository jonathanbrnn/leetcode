class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            l = target - nums[i]
            if l in hashmap and hashmap[l] != i:
                return [i, hashmap[l]]


nums = [1,3,4,54,65,7]
target = 10
print(Solution().twoSum(nums, target))
