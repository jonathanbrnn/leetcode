from typing import List
from heapq import *

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = 0
        n1 = 0
        n2 = []

        for i, j in sorted(list(zip(nums1, nums2)), key=itemgetter(1), reverse=True):
            n1 += i
            heappush(n2, i)
            if len(n2) == k:
                res = max(res, n1 * j)
                n1 -= heappop(n2)

        return res


print(Solution().maxScore([1,3,3,2], [2,1,3,4], 3))
