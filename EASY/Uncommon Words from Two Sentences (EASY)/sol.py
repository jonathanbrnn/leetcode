class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        dic = defaultdict(int)
        res = []

        for a,b in zip_longest(s1, s2, fillvalue=None):
            dic[a] += 1
            dic[b] += 1

        for item, val in dic.items():
            if val == 1 and item:
                res.append(item)

        return res
