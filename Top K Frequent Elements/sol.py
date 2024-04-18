class Solution:
    def topKFrequent(self, nums: list[int], k: int):
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        hashmap = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)
        return [item[0] for item in hashmap[:k]]


print(Solution().topKFrequent([1,1,1,2,4,3,2], 3))
