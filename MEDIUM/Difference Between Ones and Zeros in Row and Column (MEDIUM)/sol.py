from typing import List
from collections import defaultdict

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        onesRow = defaultdict(int)
        onesCol = defaultdict(int)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    onesRow[i] += 1

        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1:
                    onesCol[j] += 1

        for i in range(m):
            for j in range(n):
                total_ones = onesRow[i] + onesCol[j]
                total_zeros = (n - onesRow[i]) + (m - onesCol[j])
                grid[i][j] = total_ones - total_zeros

        return grid
