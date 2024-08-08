class Solution():
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            elif stack != []:
                match char:
                    case ")":
                        if stack[-1] == "(":
                            stack.pop(-1)
                        else:
                            return False
                    case "]":
                        if stack[-1] == "[":
                            stack.pop(-1)
                        else:
                            return False
                    case "}":
                        if stack[-1] == "{":
                            stack.pop(-1)
                        else:
                            return False
            else:
                return False

        return stack == []


s = "){"
sol = Solution()
print(sol.isValid(s))
