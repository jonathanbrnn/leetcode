class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        pos = 0

        while pos < len(command):
            if command[pos] == "G":
                res += "G"
                pos += 1
            elif command[pos] == "(" and command[pos + 1] == ")":
                res += "o"
                pos += 2
            else:
                res += "al"
                pos += 4

        return res
