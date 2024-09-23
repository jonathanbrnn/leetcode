class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = []

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens.append([tokenId, currentTime + self.timeToLive])

    def renew(self, tokenId: str, currentTime: int) -> None:
        for token in self.tokens:
            if token[0] == tokenId and token[1] > currentTime:
                token[1] = currentTime + self.timeToLive
                break

    def countUnexpiredTokens(self, currentTime: int) -> int:
        index = -1
        for i, token in enumerate(self.tokens):
            if token[1] > currentTime:
                index = i
                break

        if index == -1:
            self.tokens = []
            return 0

        self.tokens = self.tokens[index:]
        self.tokens = [token for token in self.tokens if token[1] > currentTime]

        return len(self.tokens)
