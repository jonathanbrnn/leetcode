class Codec:
    def __init__(self):
        self.urls = {}
        self.index = 0

    def encode(self, longUrl: str) -> str:
        self.urls[self.index] = longUrl
        self.index += 1
        return self.index - 1

    def decode(self, shortUrl: str) -> str:
        return self.urls[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
