class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return set.intersection(set(edges[0]), set(edges[1])).pop()
