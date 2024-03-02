class Solution:
    def subsetsWithDup(self, nums: list) -> list[list[int]]:
        sol = [[]]
        for i, num in enumerate(nums):
            if [num] not in sol:
                sol.append([num])
            current = []
            for other in nums[i:]:
                current.append(other)
                if current not in sol:
                    sol.append(current)
        return sol


nums = [1,1,2]
sol = Solution()
print(sol.subsetsWithDup(nums))
