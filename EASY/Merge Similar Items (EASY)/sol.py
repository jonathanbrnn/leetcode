class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dic = {}

        for i1 in items1:
            if i1[0] not in dic:
                dic[i1[0]] = i1[1]
            else:
                dic[i1[0]] += i1[1]

        for i2 in items2:
            if i2[0] not in dic:
                dic[i2[0]] = i2[1]
            else:
                dic[i2[0]] += i2[1]

        res = []

        for item, val in dic.items():
            res.append([item, val])

        res = sorted(res, key=lambda x: x[0])

        return res
