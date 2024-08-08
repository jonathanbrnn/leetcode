class Solution:
    def gcdOfStrings(self, string1: str, string2: str) -> str:
        def is_multiple(str1, str2):
            return str1 == str2 * (len(str1) // len(str2))

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        gcd_len = gcd(len(string1), len(string2))

        candidate = string1[:gcd_len]

        if is_multiple(string1, candidate) and is_multiple(string2, candidate):
            return candidate
        else:
            return ""
