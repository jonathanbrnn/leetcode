class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, char in enumerate(word):
            if char == ch:
                word = (word[:i+1])[::-1] + word[i+1:]
                break
        return word
