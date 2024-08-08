# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        res = head
        while head:
            n += 1
            head = head.next

        if n == 1:
            return None

        i = -1
        n = n // 2
        head = res
        while head:
            i += 1
            if i == n - 1:
                head.next = head.next.next
                break
            head = head.next

        return res
