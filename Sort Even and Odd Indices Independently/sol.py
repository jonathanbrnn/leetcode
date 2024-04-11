class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        even_indices = [i for i in range(len(nums)) if i % 2 == 0]
        odd_indices = [i for i in range(len(nums)) if i % 2 != 0]

        even_values = [nums[i] for i in even_indices]
        odd_values = [nums[i] for i in odd_indices]

        even_values.sort()
        odd_values.sort(reverse=True)

        result = []
        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(even_values[i // 2])
            else:
                result.append(odd_values[i // 2])

        return result


print(Solution().sortEvenOdd([4,1,2,3]))
