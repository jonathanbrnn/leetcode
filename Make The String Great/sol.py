class Solution():
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)


s = "leEeetcode"
print(Solution().makeGood(s))
