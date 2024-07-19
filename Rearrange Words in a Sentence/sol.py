class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.lower()
        text = text.split()
        text_sorted = sorted(text, key=lambda x: len(x))
        text_sorted[0] = text_sorted[0][:1].upper() + text_sorted[0][1:]

        return " ".join(text_sorted)


print(Solution().arrangeWords("Keep calm and code on"))
