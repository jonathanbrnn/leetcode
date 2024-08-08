import random

class GenerateTestCases():
    def genTarget(self, low, high) -> int:
        return random.randint(low, high)

    def genNums(self, low, high, length) -> list:
        nums = []
        for i in range(length):
            current = random.randint(low+1, high-1)
            nums.append(current)
        nums.sort()
        return nums

    def genNumsAlt(self, low, high, length):
        nums = set()
        while (len(nums)) < length:
            nums.add(random.randint(low, high))
        return sorted(list(nums))

    def writeToFile(self, filename, nums, target):
        with open(filename, 'w') as file:
            file.write(' '.join(map(str, nums)) + "\n")
            file.write(str(target))


nums = GenerateTestCases().genNumsAlt(-1000000, 1000000, 10000)
target = random.randint(-100000, 100000)
GenerateTestCases().writeToFile("testcases.txt", nums, target)

