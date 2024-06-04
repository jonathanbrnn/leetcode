from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = [[]]
        nums2 = set(nums2)
        for num in list(set(nums1)):
            if num not in nums2:
                res[0].append(num)
            else:
                nums2 = nums2 - {num}
        res.append(nums2)
        return res
