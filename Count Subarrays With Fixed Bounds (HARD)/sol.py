class Solution:
  def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
    ans = 0
    j = -1
    prevMinKIndex = -1
    prevMaxKIndex = -1

    for i, num in enumerate(nums):
      if num < minK or num > maxK:
        j = i
      if num == minK:
        prevMinKIndex = i
      if num == maxK:
        prevMaxKIndex = i
      ans += max(0, min(prevMinKIndex, prevMaxKIndex) - j)

    return ans



# I found this problem pretty difficult. Credit to https://algo.monster/liteproblems/2444 for the wonderful explanation!

nums = [1,1,1,1]
minK = 1
maxK = 1
sol = Solution()
print(sol.countSubarrays(nums, minK, maxK))
