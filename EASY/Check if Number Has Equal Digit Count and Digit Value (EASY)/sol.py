class Solution:
    def digitCount(self, num: str) -> bool:
        dic = defaultdict(int)

        for char in num:
            dic[int(char)] += 1

        for i in range(len(num)):
            if dic[i] != int(num[i]):
                return False

        return True
