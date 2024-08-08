# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0

        node = head
        arr = []

        while node:
            arr.append(node.val)
            node = node.next

        res = 0
        n = len(arr)

        for i in range(n):
            res = max(arr[i] + arr[n - 1 - i], res)

        return res
