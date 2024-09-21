class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        while node.next:
            curr_gcd = gcd(node.val, node.next.val)
            next = ListNode(curr_gcd, node.next)
            node.next = next
            node = next.next

        return head
