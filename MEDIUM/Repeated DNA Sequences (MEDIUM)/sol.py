class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        i = 10
        dic = defaultdict(int)
        spliced_s = s[:10]
        dic[spliced_s] += 1

        while i < len(s):
            spliced_s = spliced_s[1:] + s[i]
            dic[spliced_s] += 1
            i += 1

        res = []

        for item, val in dic.items():
            if val > 1:
                res.append(item)

        return res
