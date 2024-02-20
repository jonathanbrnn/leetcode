import random

class GenerateTestCases:
    def genTarget(self, low, high) -> int:
        return random.randint(low, high)

    def genNums(self, low, high, length) -> list:
        nums = []
        for i in range(length):
            current = random.randint(low+1, high-1)
            nums.append(current)
        return nums

    def writeToFile(self, filename, nums, target):
        with open(filename, 'w') as file:
            file.write(' '.join(map(str, nums)) + "\n")
            file.write(str(target))
