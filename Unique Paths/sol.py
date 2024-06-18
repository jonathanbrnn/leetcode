from math import factorial

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def binominal_coefficient(a, b):
            return factorial(a) // (factorial(b) * factorial(a - b))

        return binominal_coefficient(m + n - 2, m - 1)
