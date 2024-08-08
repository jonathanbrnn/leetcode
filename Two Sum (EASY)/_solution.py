numbs = [2, 7, 11, 15]
target = 22

def twoSum(nums, target):
    for n, num in enumerate(numbs):
        for c, num in enumerate(numbs):
            t = numbs[n] + numbs[c]
            if t == target:
                return n, c
