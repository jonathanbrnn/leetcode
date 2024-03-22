# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l1 = []
        while head.next is not None:
            l1.append(head.val)
            head = head.next
        l1.append(head.val)
        return l1 == l1[::-1]
