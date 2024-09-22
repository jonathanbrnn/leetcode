# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0, None)
        prev = res
        dupes = set()

        while head and head.next:
            if head.val == head.next.val:
                dupes.add(head.val)
            elif head.val not in dupes:
                prev.next = ListNode(head.val, None)
                prev = prev.next
            head = head.next

        if head and head.val not in dupes:
            prev.next = ListNode(head.val, None)

        return res.next
