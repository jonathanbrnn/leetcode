class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        current_sum = sum(arr[0: k])

        if current_sum / k >= threshold:
            res += 1

        for i in range(k, len(arr)):
            current_sum -= arr[i - k]
            current_sum += arr[i]
            if current_sum / k >= threshold:
                res += 1

        return res
