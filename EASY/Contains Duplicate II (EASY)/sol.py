'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        cou = Counter(nums)
        for i in range(n):
            # print(nums[i], cou[nums[i]])
            if cou[nums[i]] > 1:
                for j in range(i + 1, n):
                    # print(nums[i], nums[j], abs(i - j))
                    if nums[i] == nums[j] and abs(i - j) <= k:
                        return True
        return False
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic and abs(i - dic[nums[i]]) <= k:
                return True
            dic[nums[i]] = i

        return False
