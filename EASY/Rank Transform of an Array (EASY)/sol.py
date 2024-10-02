class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dic = {v : i+1 for i, v in enumerate(sorted(set(arr)))}
        return [dic[val] for val in arr]
