class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cou = Counter(arr1)
        res = []

        for num in arr2:
            for i in range(cou[num]):
                res.append(num)

        arr1.sort()

        for num in arr1:
            if num not in arr2:
                res.append(num)

        return res
