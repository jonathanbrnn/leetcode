class SmallestInfiniteSet:
    def __init__(self):
        self.smallest = 1
        self.deleted = []

    def popSmallest(self) -> int:
        if self.deleted:
            m = min(self.deleted)
            self.deleted.remove(m)
            return m
        self.smallest += 1
        return self.smallest - 1

    def addBack(self, num: int) -> None:
        if self.smallest > num and num not in self.deleted:
            self.deleted.append(num)
