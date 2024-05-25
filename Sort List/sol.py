# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        node = head
        sorted_list = []

        while node:
            sorted_list.append(node.val)
            node = node.next

        sorted_list.sort()

        node = head
        for val in sorted_list:
            node.val = val
            node = node.next

        return head
