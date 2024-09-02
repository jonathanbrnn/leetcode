class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = {5:0, 10:0}

        for bill in bills:
            if bill == 5:
                dic[5] += 1
            elif bill == 10:
                if dic[5] > 0:
                    dic[5] -= 1
                    dic[10] += 1
                else:
                    return False
            else:
                if dic[5] > 0 and dic[10] > 0:
                    dic[10] -= 1
                    dic[5] -= 1
                elif dic[5] > 2 and dic[10] == 0:
                    dic[5] -= 3
                else:
                    return False

        return True
