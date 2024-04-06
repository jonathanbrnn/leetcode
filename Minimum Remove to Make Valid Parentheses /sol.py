class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = list(s)
        replace_indices = set()
        stack = []

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    replace_indices.add(i)

        replace_indices.update(stack)

        for i in replace_indices:
            n[i] = ''

        return ''.join(n)


s = "lee(t(c)o)de)"
print(Solution().minRemoveToMakeValid(s))
