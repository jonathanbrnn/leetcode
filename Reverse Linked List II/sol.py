# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or head.next is None:
            return head

        arr = []
        i = 0
        node = head
        while node:
            i += 1
            if left <= i <= right:
                arr.append(node.val)
            node = node.next

        arr = arr[::-1]
        i = 0
        j = 0
        node = head

        while node:
            i += 1
            if left <= i <= right:
                node.val = arr[j]
                j += 1
            if i > right:
                break
            node = node.next
        return head
