# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        list2_last = None
        list1_ath = None
        list1_bth = None
        a, b = a - 1, b + 1

        node = list1
        i = 0

        while node:
            if i == a:
                list1_ath = node
            elif i == b:
                list1_bth = node
                break

            i += 1
            node = node.next

        list1_ath.next = list2
        node = list2

        while node.next:
            node = node.next

        node.next = list1_bth

        return list1
