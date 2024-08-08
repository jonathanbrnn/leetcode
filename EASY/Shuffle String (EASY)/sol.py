class Solution(object):
    def restoreString(self, s, indices):
        sol=""
        for i in range(len(s)):
            sol=sol+s[indices.index(i)]
        return sol
