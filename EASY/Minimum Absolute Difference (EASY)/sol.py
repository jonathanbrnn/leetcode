class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_diff = float('inf')
        res = []

        arr.sort()

        for i in range(1, len(arr)):
            curr_diff = arr[i] - arr[i - 1]
            if curr_diff < min_diff:
                res = [[arr[i - 1], arr[i]]]
                min_diff = curr_diff
            elif curr_diff == min_diff:
                res.append([arr[i - 1], arr[i]])

        return res
