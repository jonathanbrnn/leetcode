class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dic = defaultdict(int)
        seen = set()
        for i, char in enumerate(s):
            dic[char] = i

        for i, char in enumerate(s):
            if dic[char] == i:
                continue
            elif char in seen:
                continue
            elif abs(dic[char] - i) - 1 != distance[ord(char) - 97]:
                return False
            seen.add(char)

        return True
