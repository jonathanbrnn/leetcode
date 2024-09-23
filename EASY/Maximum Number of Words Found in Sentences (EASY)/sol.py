class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0

        for sen in sentences:
            res = max(len(sen.split()), res)

        return res
