class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res = 0
        rows = {}
        depth = 0
        for row in grid:
            depth += 1
            curr = tuple(row)
            if curr not in rows:
                rows[curr] = 1
            elif curr in rows:
                rows[curr] += 1

        for i in range(len(grid[0])):
            curr = []
            j = depth
            n = 0
            while j:
                curr.append(grid[n][i])
                n += 1
                j -= 1
            curr = tuple(curr)
            if curr in rows:
                res += rows[curr]

        return res
