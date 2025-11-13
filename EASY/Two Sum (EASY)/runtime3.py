with open("testcases.txt", "r") as f:
    x = f.readlines()
    target = int(x[1])
    print(target)
    nums = list(map(int, x[0].split()))


class Solution(object):
    def twoSum(self, nums, target):
        seen: dict[int, int] = {}

        for i, num in enumerate(nums):
            l = target - num

            if l in seen:
                return i, seen[l]
            if num not in seen:
                seen[num] = i

            if l in nums and nums.index(l) != i:
                return i, nums.index(l)


print(Solution().twoSum(nums, target))
