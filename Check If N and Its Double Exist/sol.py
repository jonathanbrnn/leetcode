class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()

        for num in arr:
            curr = num * 2
            if num * 2 in seen:
                return True
            if num % 2 == 0 and num // 2 in seen:
                return True

            seen.add(num)

        return False
