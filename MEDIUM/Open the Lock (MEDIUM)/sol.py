import heapq
from typing import Callable, List, Optional


class GraphNode:
    def __init__(
        self,
        state: str,
        parent: Optional["GraphNode"],
        steps: int,
        approximated_cost: int,
    ):
        self.state: str = state
        self.children: list["GraphNode"] = []
        self.parent: Optional["GraphNode"] = parent
        self.steps: int = steps
        self.approximated_cost: int = approximated_cost

    def expand(self, heuristic_func: Callable[[str, str], int], target: str):
        for i in range(4):
            current_digit = int(self.state[i])

            for delta in (-1, 1):
                next_digit = (current_digit + delta + 10) % 10
                state_list = list(self.state)
                state_list[i] = str(next_digit)
                next_state = "".join(state_list)

                g_cost = self.steps + 1
                h_cost = heuristic_func(next_state, target)
                f_cost = g_cost + h_cost

                self.children.append(GraphNode(next_state, self, g_cost, f_cost))

    def __lt__(self, other: "GraphNode"):
        return self.approximated_cost < other.approximated_cost

    def __eq__(self, other: object):
        if not isinstance(other, GraphNode):
            return NotImplemented
        return self.state == other.state


class Solution:
    def heuristic(self, current_state: str, target: str) -> int:
        total_distance: int = 0
        for i in range(4):
            a = int(current_state[i])
            b = int(target[i])
            diff = abs(a - b)
            total_distance += min(diff, 10 - diff)
        return total_distance

    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set(deadends)
        if "0000" in deadends_set:
            return -1
        if target == "0000":
            return 0

        root_h_cost = self.heuristic("0000", target)
        root = GraphNode("0000", None, 0, root_h_cost)
        visited = set()
        fringe = []
        heapq.heappush(fringe, root)

        while fringe:
            current_node = heapq.heappop(fringe)

            if current_node.state in deadends_set or current_node.state in visited:
                continue
            visited.add(current_node.state)

            if current_node.state == target:
                return current_node.steps

            current_node.expand(self.heuristic, target)
            for child in current_node.children:
                if child.state not in visited and child.state not in deadends_set:
                    heapq.heappush(fringe, child)

        return -1
