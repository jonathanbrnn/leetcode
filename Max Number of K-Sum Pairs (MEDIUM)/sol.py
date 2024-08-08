class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        operations = 0

        for num in nums:
            complement = k - num
            if count[num] > 0 and count[complement] > 0:
                if num != complement:
                    if count[complement] > 0:
                        count[num] -= 1
                        count[complement] -= 1
                        operations += 1
                else:
                    if count[num] > 1:
                        count[num] -= 2
                        operations += 1

        return operations
