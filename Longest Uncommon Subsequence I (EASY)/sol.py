class Solution:
    def findLUSLength(self, A: str, B: str) -> int:
        if A==B:
            return -1
        return (max(len(A), len(B)))
