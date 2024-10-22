class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        i, j = 0, len(mat[0]) - 1
        res = 0

        for row in mat:
            if i != j:
                res += row[i] + row[j]
            else:
                res += row[i]
            i += 1
            j -= 1

        return res
