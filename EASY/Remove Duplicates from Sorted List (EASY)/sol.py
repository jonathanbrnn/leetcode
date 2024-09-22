# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        arr = []
        node = head

        while node:
            if node.val not in arr:
                arr.append(node.val)
            node = node.next

        res = ListNode()
        node = res
        n = len(arr)

        for i in range(n):
            node.val = arr[i]
            if i < n - 1:
                node.next = ListNode()
                node = node.next

        return res

# Faster approach I came up while working on "Remove Duplicates from Sorted List II":
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head
