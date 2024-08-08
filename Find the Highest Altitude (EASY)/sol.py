class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        curr = 0
        for alt in gain:
            curr += alt
            res = max(res, curr)
        return res
