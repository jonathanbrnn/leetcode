with open("testcases.txt", "r") as f:
    x = f.readlines()
    target = int(x[1])
    print(target)
    nums = list(map(int, x[0].split()))


def twoSum2(self, nums, target):
    left = 0
    right = len(nums) - 1

    nums.sort()

    while left < right:
        if nums[left] + nums[right] == target:
            return nums[left], nums[right]
        if nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1


print(twoSum2(nums, target))
