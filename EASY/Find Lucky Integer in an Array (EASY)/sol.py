class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cou = Counter(arr)
        res = -1

        for item, val in cou.items():
            if item == val:
                res = max(item, res)

        return res
