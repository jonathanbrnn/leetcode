# This is a really bad solution, and there is a far more effective method where you reverse the linked list, but I honestly couldn't be bothered to do it.
# Ironically, this solution does beat over 97%, because once again, LeetCode is on crack when it comes to runtimes.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""

        while l1:
            num1 += str(l1.val)
            l1 = l1.next

        while l2:
            num2 += str(l2.val)
            l2 = l2.next

        output = str(int(num1) + int(num2))
        head = ListNode()
        node = head

        for char in output:
            node.next = ListNode()
            node = node.next
            node.val = int(char)

        return head.next
