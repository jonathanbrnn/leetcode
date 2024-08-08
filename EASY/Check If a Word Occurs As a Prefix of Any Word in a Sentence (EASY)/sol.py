class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        n = len(searchWord)
        sentence = sentence.split()

        for i, word in enumerate(sentence):
            if word[:n] == searchWord:
                return i + 1

        return -1
