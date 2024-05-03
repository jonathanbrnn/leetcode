class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version1 = [int(i) for i in version1]
        version2 = version2.split(".")
        version2 = [int(i) for i in version2]

        v1 = len(version1)
        v2 = len(version2)

        for i in range(min(v1, v2)):
            if version1[i] < version2[i]:
                return -1
            elif version1[i] > version2[i]:
                return 1

        if v1 == v2 :
            return 0
        if v1 < v2 and sum(version2[v1:]) > 0:
            return -1
        if v1 > v2 and sum(version1[v2:]) > 0:
            return 1
        return 0
