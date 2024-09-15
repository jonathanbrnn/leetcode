class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        for i in range(left, right + 1):
            i_str = str(i)
            flag = True
            if len(i_str) == 1:
                res.append(i)
            elif "0" in i_str:
                continue
            else:
                for char in i_str:
                    if i % int(char) != 0:
                        flag = False
                        break
                if flag:
                    res.append(i)

        return res
