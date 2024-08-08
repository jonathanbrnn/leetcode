class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)

        first_check = True
        second_check = True

        for a, b in zip(s1, s2):
            if a < b:
                first_check = False
            if b < a:
                second_check = False

        return (first_check and not second_check) or (second_check and not first_check)
