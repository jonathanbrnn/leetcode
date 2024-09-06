class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dic = {}

        for trip in paths:
            if trip[0] not in dic:
                dic[trip[0]] = trip[1]

        curr = paths[0][0]

        while curr in dic:
            curr = dic[curr]

        return curr
