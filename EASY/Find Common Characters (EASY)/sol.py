class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        common_letters = set(words[0])
        for word in words[1:]:
            common_letters.intersection_update(set(word))

        dic = defaultdict(lambda: float('inf'))

        for let in common_letters:
            for word in words:
                dic[let] = min(word.count(let), dic[let])

        common_letters = list(common_letters)
        for item, val in dic.items():
            if val > 1:
                for i in range(val - 1):
                    common_letters.append(item)

        return common_letters
