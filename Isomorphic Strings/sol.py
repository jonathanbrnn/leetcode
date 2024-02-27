class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = []
        map_t = []
        for char in s:
            map_s.append(s.index(char))
        for char in t:
            map_t.append(t.index(char))
        return map_t == map_s
