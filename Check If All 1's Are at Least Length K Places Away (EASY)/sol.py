class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True

        k = k + 1
        n: int = 0

        for num in nums:
            if num == 1:
                if n > 0:
                    return False
                n = k

            n -= 1

        return True
