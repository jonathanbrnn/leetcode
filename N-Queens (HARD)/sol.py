class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        def format_board(queens):
            board = []
            for queen in queens:
                row = ['.'] * n
                row[queen] = 'Q'
                board.append(''.join(row))
            return board

        def backtrack(row, queens):
            if row == n:
                solutions.append(format_board(queens))
            else:
                for col in range(n):
                    if all(col != queens[j] and
                            col - queens[j] != row - j and
                            col - queens[j] != j - row
                            for j in range(row)):
                        backtrack(row + 1, queens + [col])

        solutions = []
        backtrack(0, [])
        return solutions


sol = Solution()
x = int(input())
print(sol.solveNQueens(x))
