class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False

        has_lower = False
        has_upper = False
        has_digit = False
        has_special = False
        special_set = set("!@#$%^&*()-+")

        for i, char in enumerate(password):
            if char.islower():
                has_lower = True
            elif char.isupper():
                has_upper = True
            if char.isdigit():
                has_digit = True
            elif char in special_set:
                has_special = True
            if i > 0 and i < len(password):
                if char == password[i-1]:
                    return False

        return has_lower and has_upper and has_digit and has_special
