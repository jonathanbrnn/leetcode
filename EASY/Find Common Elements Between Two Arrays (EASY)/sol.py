class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cou1 = Counter(nums1)
        cou2 = Counter(nums2)

        res = [0, 0]

        for item, val in cou1.items():
            if item in cou2:
                res[0] += val
                res[1] += cou2[item]

        return res
