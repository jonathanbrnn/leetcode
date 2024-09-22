class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = defaultdict(list)
        res = []

        for i in range(len(groupSizes)):
            if len(dic[groupSizes[i]]) == groupSizes[i]:
                res.append(dic[groupSizes[i]])
                dic[groupSizes[i]] = []
            dic[groupSizes[i]].append(i)

        for val in dic.values():
            res.append(val)

        return res
