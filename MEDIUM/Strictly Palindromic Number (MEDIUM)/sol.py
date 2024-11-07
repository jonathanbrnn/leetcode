class Solution:
    def int_to_base(self, n, base):
        if n == 0:
            return "0"
        digits = []
        while n:
            digits.append(str(n % base))
            n //= base
        return ''.join(digits[::-1])

    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n - 1):
            curr_bin = self.int_to_base(n, i)
            if curr_bin != curr_bin[::-1]:
                return False

        return True
