class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        c = ""
        i = 0
        while len(c) <= len(s) and i < len(words):
            c += words[i]
            i += 1
            if c == s:
                return True
        else:
            return False
