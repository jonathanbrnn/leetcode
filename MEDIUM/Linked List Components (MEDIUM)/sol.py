# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)

        res = 0
        curr = False

        while head:
            if head.val in nums and not curr:
                res += 1
                curr = True
            elif head.val not in nums:
                curr = False
            head = head.next

        return res
