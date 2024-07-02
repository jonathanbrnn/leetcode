class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        cou1 = Counter(nums1)
        cou2 = Counter(nums2)

        for item, val in cou1.items():
            if item in cou2:
                for i in range(min(val, cou2[item])):
                    res.append(item)

        return res
