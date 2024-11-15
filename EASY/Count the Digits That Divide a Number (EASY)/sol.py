class Solution:
    def countDigits(self, num: int) -> int:
        digits = str(num)
        count = 0

        for digit in digits:
            if digit == "0":
                continue
            if num % int(digit) == 0:
                count += 1

        return count
