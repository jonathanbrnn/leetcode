
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def linked_list_to_array(self, node):
        array = []
        current_node = node
        while current_node is not None:
            array.append(current_node.val)
            current_node = current_node.next
        return array

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = self.linked_list_to_array(self, l1)
        list2 = self.linked_list_to_array(self, l2)

        sol1 = ''
        sol2 = ''

        for num in reversed(list1):
            sol1 += str(num)
        for num in reversed(list2):
            sol2 += str(num)
        sol = (int(sol1) + int(sol2))
        sol = str(sol)

        out_head = ListNode(0)
        current = out_head

        for i, num in enumerate(sol):
            new_node = ListNode(int(num))
            new_node.next = current.next
            current.next = new_node

        return out_head.next


