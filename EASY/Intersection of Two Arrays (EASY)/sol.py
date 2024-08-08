class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1).intersection(set(nums2)))


sol = Solution()
nums1 = [1,2,3,4,5]
nums2 = [1,3,4,23,5]
print(sol.intersection(nums1, nums2))
