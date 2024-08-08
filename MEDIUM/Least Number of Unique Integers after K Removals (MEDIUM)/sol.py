from collections import Counter
nums = [4,3,1,1,3,3,2]
k = 3

class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        cou = Counter(arr)
        sorted_cou = sorted(cou.items(), key=lambda x: x[1], reverse=False)

        while True:
            if k - sorted_cou[0][1] > 0:
                k -= sorted_cou[0][1]
                sorted_cou.remove(sorted_cou[0])
            else:
                break
        return len(sorted_cou)


newSol = Solution()
print(newSol.findLeastNumOfUniqueInts(nums, k))
