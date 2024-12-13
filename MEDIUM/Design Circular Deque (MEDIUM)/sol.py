class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = []
        self.max_size = k

    def insertFront(self, value: int) -> bool:
        if self.max_size >= len(self.deque) + 1:
            self.deque.insert(0, value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.max_size >= len(self.deque) + 1:
            self.deque.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if len(self.deque) > 0:
            del self.deque[0]
            return True
        return False

    def deleteLast(self) -> bool:
        if len(self.deque) > 0:
            del self.deque[-1]
            return True
        return False

    def getFront(self) -> int:
        if len(self.deque) > 0:
            return self.deque[0]
        return -1

    def getRear(self) -> int:
        if len(self.deque) > 0:
            return self.deque[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.deque) == 0

    def isFull(self) -> bool:
        return self.max_size == len(self.deque)



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
