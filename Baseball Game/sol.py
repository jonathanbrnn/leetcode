from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = [0]
        last = 0
        for i in range(len(operations)):
            if operations[i].lstrip('-').isdigit():
                res.append(int(operations[i]))
            elif operations[i] == '+':
                res.append(res[-1] + res[-2])
            elif operations[i] == 'D':
                res.append(res[-1] * 2)
            else:
                res.pop()

        return sum(res)
