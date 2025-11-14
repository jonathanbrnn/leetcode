def compare(a: str, b: str) -> int:
    if a + b > b + a:
        return -1
    else:
        return 1


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums: list[str] = sorted([str(num) for num in nums], key=cmp_to_key(compare))

        res: str = "".join(nums)
        return "0" if res[0] == "0" else res
