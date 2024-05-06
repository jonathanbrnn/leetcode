# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, node: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while node:
            while stack and stack[-1].val < node.val:
                stack.pop()
            stack.append(node)
            node = node.next

        nxt = None
        while stack:
            node = stack.pop()
            node.next = nxt
            nxt = node

        return node
