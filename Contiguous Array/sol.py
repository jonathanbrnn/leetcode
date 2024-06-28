class Solution:
    def findMaxLength(self, nums) -> int:
        sum_index = {0: -1}
        current = max_length = 0

        for i, num in enumerate(nums):
            current += 1 if num == 1 else -1

            if current in sum_index:
                max_length = max(max_length, i - sum_index[current])
            else:
                sum_index[current] = i

        return max_length
