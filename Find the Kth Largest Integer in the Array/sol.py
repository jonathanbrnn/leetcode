class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        res = [eval(i) for i in nums]
        res = sorted(res)
        indexK = len(res) - k
        return str(res[indexK])


nums = ["2","21","12","1"]
k = 3
sol = Solution()
print(sol.kthLargestNumber(nums, k))
