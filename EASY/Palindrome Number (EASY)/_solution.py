class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == "".join(reversed(s))


# Better solution:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        original: int = x
        reverse: int = 0

        while x > 0:
            digit = x % 10
            reverse = (reverse * 10) + digit

            x //= 10

        return original == reverse
