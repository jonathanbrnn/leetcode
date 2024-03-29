from collections import Counter

class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_num = max(nums)
        ans = 0
        count = 0
        j = 0
        for i in range(n):
            if nums[i] == max_num:
                count += 1
            while count >= k:
                if nums[j] == max_num:
                    count -= 1
                j += 1
            ans += j
        return ans



nums = [2,2,2,2,1,3,3,2,2,1,1,3,1,1,2,3,2,1,1,2,1,1,2,1,2,1,2,1,3,1,3,3]
k = 3
sol = Solution()
print(sol.countSubarrays(nums, k))
