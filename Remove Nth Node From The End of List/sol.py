# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLength(self, node) -> int:
        length = 1
        while node.next is not None:
            length += 1
            node = node.next
        return length

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        toRemove = self.getLength(head) - n
        current = 0
        node = head
        if toRemove == 0:
            return head.next
        while True:
            current += 1
            if current == toRemove:
                node.next = node.next.next
            if node.next is None:
                break
            else:
                node = node.next
        return head
