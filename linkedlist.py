from typing import Optional


class Node:
    def __init__(self):
        self.val = 0
        self.next = None


class LinkedList:
    def __init__(self):
        pass

    def createLinkedList(self, nums: list):
        if not nums:
            return None

        head = Node()
        node = head
        for i, num in enumerate(nums):
            node.val = num
            if i < len(nums) - 1:
                node.next = Node()
                node = node.next
        return head

    def createArray(self, node: Node) -> list:
        arr = []
        while node is not None:
            arr.append(node.val)
            node = node.next
        return arr

    def traverse(self, node: Node):
        while node is not None:
            print(node.val)
            node = node.next

    def mergeTwoLinkedLists(self, node1: Optional[Node], node2: Optional[Node]):
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

        if node1 is not None:
            current.next = node1
        elif node2 is not None:
            current.next = node2

        return merged.next 


arr1 = [1, 2, 3, 4, 5, 6, 6, 6, 6]
arr2 = [-1, 0, 1]
linkedList = LinkedList()

l1 = linkedList.createLinkedList(arr1)
l2 = linkedList.createLinkedList(arr2)
l3 = linkedList.mergeTwoLinkedLists(l1, l2)
arr3 = linkedList.createArray(l3)
print(arr3)
