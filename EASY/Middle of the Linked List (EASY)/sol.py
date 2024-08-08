# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMiddle(self, node) -> int:
        i = 1
        while node.next is not None:
            node = node.next
            i += 1
        if i % 2 == 0:
            i = i // 2 + 1
        else:
            i = int((i/2) + 0.5)
        return i

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = self.findMiddle(head)
        node = head
        while middle > 1:
            node = node.next
            middle -= 1
        return node
