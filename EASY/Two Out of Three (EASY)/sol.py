class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        occ = {}

        for n1, n2, n3 in zip_longest(set(nums1), set(nums2), set(nums3), fillvalue=None):
            if n1:
                if n1 not in occ:
                    occ[n1] = 1
                else:
                    occ[n1] += 1
            if n2:
                if n2 not in occ:
                    occ[n2] = 1
                else:
                    occ[n2] += 1
            if n3:
                if n3 not in occ:
                    occ[n3] = 1
                else:
                    occ[n3] += 1

        res = []

        for item, val in occ.items():
            if val >= 2:
                res.append(item)

        return res
