class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x:x[1], reverse = True)

        res = 0

        for i, j in boxTypes:
            if i < truckSize:
                res += i * j
                truckSize -= i
            else:
                res += truckSize * j
                break

        return res
