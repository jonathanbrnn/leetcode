# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def linked_list_to_array(self, node):
        array = []
        current_node = node
        while current_node is not None:
            array.append(current_node.val)
            current_node = current_node.next
        return array

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.linked_list_to_array(list1)
        l2 = self.linked_list_to_array(list2)
        l3 = []

        for index, n in enumerate(l1):
            if n < l2[index]:
                l3.append(n)
            else:
                l3.append(l2[index])

        print(l3)