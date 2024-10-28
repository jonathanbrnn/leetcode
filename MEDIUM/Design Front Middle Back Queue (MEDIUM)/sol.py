# This was my first approach using a LinkedList. It took me 30 - 45 min to figure it out.
# Runtime: [86ms, 17.48mb]

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class FrontMiddleBackQueue:

    def __init__(self):
        self.head = ListNode()
        self.length = 0

    def pushFront(self, val: int) -> None:
        new_node = ListNode(val, self.head.next)
        self.head.next = new_node
        self.length += 1

    def pushMiddle(self, val: int) -> None:
        middle = self.length // 2
        node = self.head

        for _ in range(middle):
            node = node.next

        new_node = ListNode(val, node.next)
        node.next = new_node
        self.length += 1

    def pushBack(self, val: int) -> None:
        node = self.head
        while node.next:
            node = node.next

        node.next = ListNode(val, None)
        self.length += 1

    def popFront(self) -> int:
        if self.length == 0:
            return -1

        removed_val = self.head.next.val
        self.head.next = self.head.next.next
        self.length -= 1
        return removed_val

    def popMiddle(self) -> int:
        if self.length == 0:
            return -1

        if self.length == 1:
            removed_val = self.head.next.val
            self.head.next = None
            self.length -= 1
            return removed_val

        if self.length == 2:
            removed_val = self.head.next.val
            self.head.next = self.head.next.next
            self.length -= 1
            return removed_val

        middle = (self.length - 1) // 2
        node = self.head

        for _ in range(middle):
            node = node.next

        removed_val = node.next.val
        node.next = node.next.next
        self.length -= 1
        return removed_val

    def popBack(self) -> int:
        if self.length == 0:
            return -1

        node = self.head

        if self.length == 1:
            removed_val = node.next.val
            node.next = None
            self.length -= 1
            return removed_val

        while node.next.next:
            node = node.next

        removed_val = node.next.val
        node.next = None
        self.length -= 1
        return removed_val

# And this is the disgustingly easy way to do it. Runtime: [59ms, 17.36mb]:

class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = []

    def pushFront(self, val: int) -> None:
        self.queue.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        middle = len(self.queue) // 2
        self.queue.insert(middle, val)

    def pushBack(self, val: int) -> None:
        self.queue.append(val)

    def popFront(self) -> int:
        if self.queue:
            return self.queue.pop(0)
        return -1

    def popMiddle(self) -> int:
        if self.queue:
            middle = (len(self.queue) - 1) // 2
            return self.queue.pop(middle)
        return -1

    def popBack(self) -> int:
        if self.queue:
            return self.queue.pop()
        return -1

# This took me about 5 minutes and is really easy because of Python's built-in insert() and pop() functions.
# When trying to solve this problem, I'd recommend either trying to solve it using a variation of a LinkedList
# or using a double-ended queue.
