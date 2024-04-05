with open("testcases.txt", "r") as f:
    x = f.readlines()
    target = int(x[1])
    print(target)
    nums = list(map(int, x[0].split()))


def twoSum(target, nums):
    for i in nums:
        for j in nums:
            t = i + j
            if t == target:
                return i, j


print(twoSum(target, nums))
