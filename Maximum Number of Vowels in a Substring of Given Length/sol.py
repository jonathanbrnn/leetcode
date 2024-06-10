class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = "aeiou"

        stack = []
        vowel_count = 0
        res = 0

        for i in range(len(s)):
            if i < k:
                if s[i] in vowels:
                    vowel_count += 1
                stack.append(s[i])
                res = max(res, vowel_count)
            else:
                print(stack, vowel_count)
                if s[i] in vowels:
                    vowel_count += 1
                if stack[0] in vowels:
                    vowel_count -= 1
                stack.append(s[i])
                stack.pop(0)
                res = max(res, vowel_count)

        return res


print(Solution().maxVowels("ibpbhixfiouhdljnjfflpapptrxgcomvnb", 33))
