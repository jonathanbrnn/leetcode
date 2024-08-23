class MedianFinder:

    def __init__(self):
        self.stream = []

    def addNum(self, num: int) -> None:
        self.stream.append(num)

    def findMedian(self) -> float:
        length_stream = len(self.stream)
        self.stream = sorted(self.stream)

        if length_stream % 2 == 0:
            return (self.stream[length_stream // 2 - 1] + self.stream[length_stream // 2]) / 2
        else:
            return (self.stream[int(length_stream / 2 - 0.5)])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
ü
