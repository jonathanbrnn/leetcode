class StackNode:
    def __init__(self):
        self.val = None
        self.next = None


class MinStack:
    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        to_add = StackNode()
        to_add.val = val

        if self.head:
            to_append = self.head
            to_add.next = to_append
            self.head = to_add
        else:
            self.head = to_add

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        node = self.head
        min_val = None

        while node:
            if min_val != None:
                min_val = min(min_val, node.val)
            else:
                min_val = node.val
            node = node.next

        return min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
