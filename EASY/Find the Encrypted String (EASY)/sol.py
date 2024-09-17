class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        res = []

        for i in range(n):
            curr = (i + k) % n
            res.append(s[curr])

        return "".join(res)
