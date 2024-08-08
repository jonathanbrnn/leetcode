class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0
        for word in words:
            current = chars
            good = True
            length = 0
            for char in word:
                length += 1
                if char in current:
                    current = current.replace(char, "", 1)
                else:
                    good = False
                    break
            if good:
                total += length

        return total
