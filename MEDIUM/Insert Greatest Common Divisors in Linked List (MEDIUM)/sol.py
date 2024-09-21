class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node.next:
            curr_gcd = gcd(node.val, node.next.val)
            next = ListNode()
            next.val = curr_gcd
            second = node.next
            next.next = second
            node.next = next
            node = node.next.next

        return head
