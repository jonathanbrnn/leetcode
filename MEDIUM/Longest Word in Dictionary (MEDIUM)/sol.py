class Solution:
    def longestWord(self, words: List[str]) -> str:
        longest = sorted(words, key=lambda x: (-len(x), x))
        words_set = set(words)
        res = ""

        for w in longest:
            curr = ""
            valid = True
            for char in w:
                curr += char
                if curr not in words_set:
                    valid = False
                    break

            if valid and (len(w) > len(res) or (len(w) == len(res) and w < res)):
                res = w

        return res
