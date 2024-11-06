class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        bannedWords = set(bannedWords)
        banned_count = 0

        for word in message:
            if word in bannedWords:
                banned_count += 1
            if banned_count == 2:
                return True

        return False
