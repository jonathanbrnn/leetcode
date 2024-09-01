class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l_count = moves.count("L")
        r_count = moves.count("R")
        _count = moves.count("_")

        return max((l_count + _count) - r_count, (r_count + _count) - l_count)
