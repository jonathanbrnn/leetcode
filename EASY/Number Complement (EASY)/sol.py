class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)
        binary_rep = ""

        for char in num[2:]:
            if char == "1":
                binary_rep += "0"
            else:
                binary_rep += "1"

        return int(binary_rep, 2)
