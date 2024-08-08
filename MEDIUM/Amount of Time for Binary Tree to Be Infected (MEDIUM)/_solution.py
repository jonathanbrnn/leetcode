inp = [1, 5, 3, None, 4, 10, 6, 9, 2]
target = 3

def calcSpread(nums: list, target: int) -> int:
    time = 0
    startingPoint = nums.index(target)
    rootVal = nums[0]

    upTree(nums, startingPoint, time)

    return time


def upTree(nums: list, index, time):
    time += 1
    if index % 2 == 0:
        (index / 2) - 1
    else:
        (index / 2) - 0.5
    if index > 0:


