class Solution:
    def maxDepth(self, s: str) -> int:
        if len(s) == 0:
            return 0
        depth = counter = 0
        for char in s:
            if char == "(":
                counter += 1
                depth = max(depth, counter)
            elif char == ")":
                counter -= 1
                depth = max(depth, counter)

        return depth


s = "(1)+((2))+(((3)))"
print(Solution().maxDepth(s))
