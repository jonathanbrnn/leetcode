class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i, word in enumerate(words):
            w = words[:i] + words[i+1:]
            current = " ".join(w)
            if word in current:
                res.append(word)
        return res
