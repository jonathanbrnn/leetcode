class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(50000)
        s = int("".join(str(n) for n in num))
        t = s+k
        return list(int(i) for i in str(t))
