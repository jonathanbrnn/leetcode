# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        res = []
        while head:
            current_value = head.val
            found = False
            curr = head
            while curr:
                if curr.val > current_value:
                    res.append(curr.val)
                    found = True
                    break
                curr = curr.next
            if found == False:
                res.append(0)
            head = head.next
        return res
