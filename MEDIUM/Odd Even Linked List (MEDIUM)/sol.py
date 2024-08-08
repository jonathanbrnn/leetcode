class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        node = head
        i = 1
        even = []
        odd = []

        while node:
            if i % 2 == 0:
                even.append(node.val)
            else:
                odd.append(node.val)
            node = node.next
            i += 1

        odd += even
        node = head

        for i in range(len(odd)):
            node.val = odd[i]
            node = node.next

        return head
