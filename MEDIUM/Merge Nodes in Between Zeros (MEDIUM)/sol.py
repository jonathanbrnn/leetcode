# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head.next
        curr_sum = 0
        new_list_head = ListNode()
        new_list = new_list_head


        while node:
            if node.val == 0:
                new_list.next = ListNode(curr_sum)
                new_list = new_list.next
                curr_sum = 0
            else:
                curr_sum += node.val
            node = node.next

        return new_list_head.next
