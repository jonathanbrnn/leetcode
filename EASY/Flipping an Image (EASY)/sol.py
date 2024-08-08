class Solution:
    def flipAndInvertImage(self, image: list[list[int]]):
        [i.reverse() for i in image]
        res = []
        for row in image:
            current = []
            for pixel in row:
                print(pixel)
                if pixel == 1:
                    current.append(0)
                else:
                    current.append(1)
            res.append(current)
        return res


print(Solution().flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
