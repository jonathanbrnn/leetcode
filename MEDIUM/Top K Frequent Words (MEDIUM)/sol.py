class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cou = Counter(words)
        words = sorted(list(set(words)))
        words = sorted(words, key=lambda x: cou[x], reverse=True)
        return words[:k]
