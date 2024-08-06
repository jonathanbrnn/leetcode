class Solution:
    def minimumPushes(self, word: str) -> int:
        cou = [0] * 26

        for char in word:
            cou[ord(char) - 97] += 1

        cou = sorted(cou, reverse=True)

        res = 0

        for i in range(len(cou)):
            if cou[i] == 0:
                break
            res += (i // 8 + 1) * cou[i]

        return res


print(Solution().minimumPushes("aabbccddeeffgghhiiiiii"))
