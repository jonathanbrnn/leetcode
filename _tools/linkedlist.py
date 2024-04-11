from typing import Optional


class Node:
    def __init__(self):
        self.val = 0
        self.next = None
        # self.previous = None


def createLinkedList(nums: list, sortList: bool = False):
    if not nums:
        return None

    try:
        if sortList:
            nums.sort()
    except TypeError:
        pass
    head = Node()
    node = head
    for i, num in enumerate(nums):
        node.val = num
        if i < len(nums) - 1:
            node.next = Node()
            # node.next.previous = node
            node = node.next
    return head


def createArray(node: Node, sortArray: bool = False) -> list:
    arr = []
    while node is not None:
        arr.append(node.val)
        node = node.next
    if sortArray:
        arr.sort()
    return arr


def mergeTwoLinkedLists(node1: Optional[Node], node2: Optional[Node]) -> Optional[Node]:
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


def getLength(node: Optional[Node]) -> int:
    length = 1
    while node.next is not None:
        length += 1
        node = node.next
    return length


def index(node: Optional[Node], i: int) -> Optional[Node]:
    try:
        if i == 0:
            return node
        elif i > 0:
            while i > 0:
                node = node.next
                i -= 1
            return node
        else:
            length = getLength(node)
            length += i
            print(length)
            while length > 0:
                node = node.next
                length -= 1
            return node
    except AttributeError:
        print("WARNING: Index out of bounds")
        return None


def delete(head: Optional[Node], i: int):
    node = head
    if i == 0:
        node = node.next
        return node
    else:
        nodeBeforeDeletion = index(node, i - 1)
        if nodeBeforeDeletion.next.next is not None:
            nodeBeforeDeletion.next = nodeBeforeDeletion.next.next
        else:
            nodeBeforeDeletion.next = None
        return node


def reverse(node: Optional[Node]) -> Optional[Node]:
    prev = None
    current = node
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev


def traverse(node: Optional[Node]):
    while node.next is not None:
        print(node.val)
        node = node.next
    print(node.val)


def insert(node: Optional[Node], i, value):
    if i == 0:
        inserted = Node()
        inserted.val = value
        inserted.next = node
        node = inserted
    else:
        inserted = Node()
        inserted.val = value
        current = index(node, i)
        inserted.next = current
        prev = index(node, i - 1)
        prev.next = inserted
    return node


def createLoop(node):
    head = node
    while node.next is not None:
        node = node.next
    node.next = head
    return head


def detectLoop(head) -> bool:
    rabbit = turtle = head
    while rabbit is not None and rabbit.next is not None:
        turtle = turtle.next
        rabbit = rabbit.next.next
        if rabbit == turtle:
            return True
    return False


arr1 = [1, 2, 3, 4, 5, 6, 6, 6, 6]
arr2 = [21, 56, 89, 100]
l1 = createLinkedList(arr1)
l2 = createLinkedList(arr2)
print(createArray(l2))
l2 = insert(l2, 0, 34256789)
print(createArray(l2))
l3 = mergeTwoLinkedLists(l1, l2)
print(createArray(l3, True))
l3 = delete(l3, 3)
print(createArray(l3))
l4 = createLinkedList([1,2,3,4,5,6,7,8,9])
print(traverse(l4))
