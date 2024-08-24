# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        occ = set(nums)

        while node.val in occ:
            head = node.next
            node = node.next

        node = head
        prev = head

        while node:
            if node.val in occ:
                prev.next = node.next
            else:
                prev = node
            node = node.next

        return head
