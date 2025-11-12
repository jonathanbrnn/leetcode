class Solution:
    def convert(self, s: str, rows: int) -> str:
        if not s or rows == 0:
            return ""
        if rows == 1 or rows >= len(s):
            return s

        n = len(s)
        cols = n
        zigzag = [[""] * cols for _ in range(rows)]

        c = 0
        i = 0
        j = 0
        go_down = True

        while c < n:
            zigzag[i][j] = s[c]
            c += 1

            if i == 0:
                go_down = True
            elif i == rows - 1:
                go_down = False

            if go_down:
                i += 1
            else:
                i -= 1
                j += 1

        res = ""
        for row in zigzag:
            for char in row:
                if char != "":
                    res += char
        return res
