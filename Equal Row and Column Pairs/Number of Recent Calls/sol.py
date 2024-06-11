class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests:
            if self.requests[0] < t - 3000:
                self.requests.pop(0)
            else:
                break
        return len(self.requests)
