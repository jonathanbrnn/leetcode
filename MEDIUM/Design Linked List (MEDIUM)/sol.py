class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1

        traverse = self.head
        for i in range(index):
            traverse = traverse.next

        return traverse.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)

        if self.head:
            new_node.next = self.head
        else:
            self.tail = new_node

        self.head = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node

        self.tail = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return

        if index == 0:
            self.addAtHead(val)
            return

        if index == self.length:
            self.addAtTail(val)
            return

        new_node = Node(val)
        traverse = self.head

        for i in range(index - 1):
            traverse = traverse.next

        new_node.next = traverse.next
        traverse.next = new_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return

        if index == 0:
            self.head = self.head.next
            if self.length == 1:
                self.tail = None
            self.length -= 1
            return

        traverse = self.head
        for i in range(index - 1):
            traverse = traverse.next

        traverse.next = traverse.next.next

        if index == self.length - 1:
            self.tail = traverse

        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
