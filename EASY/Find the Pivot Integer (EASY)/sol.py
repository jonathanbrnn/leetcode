class Solution:
    def pivotInteger(self, n: int) -> int:
        current_sum = 0
        total_sum = sum(range(1, n + 1))
        for i in range(1, n + 1):
            current_sum += i
            if current_sum == total_sum:
                return i
            else:
                total_sum -= i
        return -1


sol = Solution()
print(sol.pivotInteger(1))


# BETTER SOLUTION


class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = n * (n + 1) // 2
        pivot = int(math.sqrt(total_sum))

        if pivot * pivot == total_sum:
            return pivot

        return -1
