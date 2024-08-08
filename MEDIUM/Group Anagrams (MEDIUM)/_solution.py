from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            sorted_word_tuple = tuple(sorted(word))
            anagrams[sorted_word_tuple].append(word)
        return list(anagrams.values())