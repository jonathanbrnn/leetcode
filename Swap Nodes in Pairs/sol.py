# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head

        nodes = []
        node = head

        while node:
            nodes.append(node.val)
            node = node.next

        i = 0
        j = 1
        swapped_pairs = []
        n = len(nodes)
        if n % 2 != 0:
            n -= 1

        while j < n:
            swapped_pairs.append(nodes[j])
            swapped_pairs.append(nodes[i])
            j += 2
            i += 2

        res = head
        for value in swapped_pairs:
            head.val = value
            head = head.next

        return res
