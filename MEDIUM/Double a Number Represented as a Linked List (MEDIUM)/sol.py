# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        head = self.reverseList(head)

        node = head
        carry = 0

        while node:
            doubled_value = node.val * 2 + carry
            node.val = doubled_value % 10
            carry = doubled_value // 10

            if not node.next and carry:
                node.next = ListNode(carry)
                break

            node = node.next

        return self.reverseList(head)


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
