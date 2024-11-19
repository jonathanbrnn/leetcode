class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        columns = defaultdict(int)
        rows = defaultdict(int)

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                columns[j] = max(columns[j], cell)
                rows[i] = max(rows[i], cell)

        total_sum = 0

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                total_sum += abs(cell - min(columns[j], rows[i]))

        return total_sum
