inp = [2, 3, 1, 1, 4]


def findJumps(nums):
    n = len(nums)
    if n < 2:
        return 0

    maxPos = nums[0]
    maxSteps = nums[0]
    jumps = 1

    for i in range(1, n):
        if maxSteps < i:
            jumps += 1
            maxSteps = maxPos
        maxPos = max(maxPos, nums[i] + i)

    return jumps


print(findJumps(inp))
