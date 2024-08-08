# This might be the easiest leetcode problem ever

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        jewels_set = set(list(jewels))

        for i in range(len(stones)):
            if stones[i] in jewels_set:
                res += 1

        return res
