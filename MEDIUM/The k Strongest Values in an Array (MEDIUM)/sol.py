from typing import List

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()

        n = len(arr)
        m = arr[((n - 1) // 2)]

        arr = sorted(arr, key=lambda x: (abs(x - m), x), reverse=True)

        return arr[:k]
