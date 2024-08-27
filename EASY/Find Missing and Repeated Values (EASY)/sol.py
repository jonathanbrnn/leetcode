class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        all_n = [i for i in range(1, (len(grid) * len(grid)) + 1)]
        dic = {}
        a = 0
        b = 0

        for col in grid:
            for cell in col:
                if cell not in dic:
                    dic[cell] = 1
                else:
                    a = cell

        for i in all_n:
            if i not in dic:
                b = i

        return [a, b]
