class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [i for i in range(1, m + 1)]
        res = []

        for num in queries:
            index = p.index(num)
            del p[index]
            p.insert(0, num)
            res.append(index)

        return res
