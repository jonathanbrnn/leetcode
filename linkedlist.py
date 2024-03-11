from typing import Optional


class Node:
    def __init__(self):
        self.val = 0
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        pass

    def createLinkedList(self, nums: list, sort: bool):
        if not nums:
            return None

        try:
            if sort:
                nums.sort()
        except TypeError:
            pass
        head = Node()
        node = head
        for i, num in enumerate(nums):
            node.val = num
            if i < len(nums) - 1:
                node.next = Node()
                node.next.previous = node
                node = node.next
        return head

    def createArray(self, node: Node) -> list:
        arr = []
        while node is not None:
            arr.append(node.val)
            node = node.next
        return arr

    def mergeTwoLinkedLists(self, node1: Optional[Node], node2: Optional[Node]) -> Optional[Node]:
        merged = Node()
        current = merged
        while node1 is not None and node2 is not None:
            if node1.val <= node2.val:
                current.next = node1
                node1 = node1.next
            else:
                current.next = node2
                node2 = node2.next
            current = current.next

        # If there are remaining nodes in either linked list, append them to the end of the merged linked list
        current.next = node1 or node2

        return merged.next

    def linkedListLength(self, node: Optional[Node]) -> int:
        length = 1
        while node.next is not None:
            length += 1
            node = node.next
        return length

    def index(self, node: Optional[Node], i: int) -> Optional[Node]:
        try:
            if i == 0:
                return node
            elif i > 0:
                while i > 0:
                    node = node.next
                    i -= 1
                return node
            else:
                length = self.linkedListLength(node)
                length += i
                print(length)
                while length > 0:
                    node = node.next
                    length -= 1
                return node
        except AttributeError:
            print("WARNING: Index out of bounds")
            return None

    def delete(self, node: Optional[Node], i: int):
        if i == 0:
            node = node.next
            return node
        else:
            nodeBeforeDeletion = self.index(node, i - 1)
            if nodeBeforeDeletion.next.next is not None:
                nodeBeforeDeletion.next = nodeBeforeDeletion.next.next
            else:
                nodeBeforeDeletion.next = None
            return node

    def createLoop(self, node):
        head = node
        while node.next is not None:
            node = node.next
        node.next = head
        return head

    def detectLoop(self, node) -> bool:
        rabbit = turtle = node
        while rabbit is not None and rabbit.next is not None:
            turtle = turtle.next
            rabbit = rabbit.next.next
            if rabbit == turtle:
                return True
        return False


arr1 = [1, 2, 3, 4, 5, 6, 6, 6, 6]
arr2 = [21, 56, 89, 100]
linkedList = LinkedList()

l1 = linkedList.createLinkedList(arr1, True)
l2 = linkedList.createLinkedList(arr2, True)
nodeAtIndex = linkedList.index(l2, 0)

l3 = linkedList.mergeTwoLinkedLists(l1, l2)
print(linkedList.createArray(l3))

print(linkedList.detectLoop(l3))
