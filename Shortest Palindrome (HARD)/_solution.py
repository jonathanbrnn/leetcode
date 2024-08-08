s = "aacecaaa"
output = "aaacecaaa"

def create_palindrome(s):
    rev_s = s[::-1]
    for i in range(len(s), -1, -1):
        if s.startswith(rev_s[len(s)-i:]):
            return rev_s[:len(s)-i] + s

sol = create_palindrome(s)

if sol == output:
    print("Testcase passed")
else:
    print("Testcase failed")