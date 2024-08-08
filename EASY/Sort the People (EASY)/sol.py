class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = {}
        heights_length = len(heights)
        for i in range(heights_length):
            if heights[i] not in n:
                n[heights[i]] = names[i]
        res = [0] * heights_length
        heights.sort()
        heights.reverse()
        for i, height in enumerate(heights):
            res[i] = n[height]
        return res
