class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        flag = False
        res = ""

        for char in num:
            if char == "6" and not flag:
                res += "9"
                flag = True
            else:
                res += char

        return int(res)
