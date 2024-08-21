class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen = [words[0][::-1]]
        res = 0

        for word in words[1:]:
            if word in seen:
                res += 1
            seen.append(word[::-1])

        return res
