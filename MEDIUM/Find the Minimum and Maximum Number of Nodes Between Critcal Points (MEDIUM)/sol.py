class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        first_critical = None
        last_critical = None
        idx = 1
        prev = head
        curr = head.next

        min_distance = float('inf')
        max_distance = -float('inf')

        while curr.next:
            if (prev.val < curr.val > curr.next.val) or (prev.val > curr.val < curr.next.val):
                if first_critical is None:
                    first_critical = idx
                else:
                    min_distance = min(min_distance, idx - last_critical)
                    max_distance = idx - first_critical

                last_critical = idx

            prev = curr
            curr = curr.next
            idx += 1

        if min_distance == float('inf'):
            min_distance = -1

        if max_distance == -float('inf'):
            max_distance = -1

        return [min_distance, max_distance]
