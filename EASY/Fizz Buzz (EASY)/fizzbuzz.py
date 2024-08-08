import random
class Solution:
    def fizzBuzz(self, nums: list[int]) -> list[str]:
        result = []
        for i in range(1, nums[0] + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

filepath = '/Users/jonathan/PycharmProjects/leetcode/testcases.txt'
with open(filepath, 'w') as f:
    for i in range(-1, 1000):
        r = random.randint(1, 1000)
        f.write(f'{r}\n')

sol = []
with open(filepath, 'r') as f:
    for line in f:
        sol.append(int(line.strip()))

filepath = '/Users/jonathan/PycharmProjects/leetcode/testcasesExpected.txt'
with open(filepath, 'w') as f:
    for i in range(len(sol)-1)

newSol = Solution()
print(newSol.fizzBuzz(sol))
