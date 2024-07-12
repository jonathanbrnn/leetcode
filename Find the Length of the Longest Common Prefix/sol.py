class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        res = 0
        dic = {}

        for i in range(len(arr1)):
            curr = str(arr1[i])
            for i in range(len(curr) + 1):
                if curr[:i] not in dic:
                    dic[curr[:i]] = i

        for i in range(len(arr2)):
            curr = str(arr2[i])
            for i in range(len(curr) - 1, -1, -1):
                if curr in dic:
                    res = max(res, dic[curr])
                    break
                curr = curr[:-1]

        return res
