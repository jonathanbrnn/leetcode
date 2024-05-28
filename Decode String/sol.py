class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currentNumber = ''
        currentString = ''

        for char in s:
            if char.isdigit():
                currentNumber += char
            elif char == '[':
                stack.append((int(currentNumber), currentString))
                currentNumber, currentString = '', ''
            elif char.isalpha():
                currentString += char
            elif char == ']':
                num, prevString = stack.pop()
                currentString = prevString + num * currentString

        return currentString
