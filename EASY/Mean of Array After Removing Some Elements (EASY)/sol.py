class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        per = (n * 5) // 100
        arr.sort()
        sm = 0

        for i in range(per, n - per):
            sm += arr[i]

        return sm / (n - (2 * per))
