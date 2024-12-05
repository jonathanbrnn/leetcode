class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ships = {}
        count = 0

        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    flag = False
                    try:
                        if board[i - 1][j] == "X":
                            ships[(i, j)] = ships[(i - 1, j)]
                            flag = True
                    except:
                        pass

                    try:
                        if board[i][j - 1] == "X":
                            ships[(i, j)] = ships[(i, j - 1)]
                            flag = True
                    except:
                        pass

                    if not flag:
                        ships[(i,j)] = count
                        count += 1

        print(ships)

        indv = set()

        for val in ships.values():
            indv.add(val)

        return len(indv)
