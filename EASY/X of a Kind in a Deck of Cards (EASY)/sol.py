class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        gcd = reduce(math.gcd, Counter(deck).values())
        return gcd > 1
