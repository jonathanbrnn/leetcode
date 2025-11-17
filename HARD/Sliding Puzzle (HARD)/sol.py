import heapq
from typing import List, Optional


class GraphNode:
    def __init__(
        self, parent: Optional["GraphNode"], state: list[list[int]], steps: int
    ):
        self.parent: Optional["GraphNode"] = parent
        self.children: List[Optional["GraphNode"]] = []
        self.state: list[list[int]] = state
        self.id: str = f"{self.state[0][0]}{self.state[0][1]}{self.state[0][2]}{self.state[1][0]}{self.state[1][1]}{self.state[1][2]}"
        self.steps: int = steps
        self.zero_pos: list[int] = []
        self.approximated_cost: int = self.heuristic() + self.steps

    def heuristic(self) -> int:
        total_manhattan_distance: int = 0

        target_dict: dict[int, list[int]] = {
            1: [0, 0],
            2: [0, 1],
            3: [0, 2],
            4: [1, 0],
            5: [1, 1],
            0: [1, 2],
        }

        for i in range(2):
            for j in range(3):
                current_tile: int = self.state[i][j]

                if current_tile == 0:
                    self.zero_pos.append(i)
                    self.zero_pos.append(j)

                total_manhattan_distance += abs(j - target_dict[current_tile][1]) + abs(
                    i - target_dict[current_tile][0]
                )

        return total_manhattan_distance

    def expand(self):
        i: int = self.zero_pos[0]
        j: int = self.zero_pos[1]

        above: bool = i == 1
        below: bool = i == 0
        left: bool = j > 0
        right: bool = j < 2

        if above:
            new_state: list[list[int]] = copy.deepcopy(self.state)
            new_state[i][j], new_state[0][j] = new_state[0][j], new_state[i][j]

            self.children.append(GraphNode(self, new_state, self.steps + 1))

        if below:
            new_state: list[list[int]] = copy.deepcopy(self.state)
            new_state[i][j], new_state[1][j] = new_state[1][j], new_state[i][j]

            self.children.append(GraphNode(self, new_state, self.steps + 1))

        if left:
            new_state: list[list[int]] = copy.deepcopy(self.state)
            new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]

            self.children.append(GraphNode(self, new_state, self.steps + 1))

        if right:
            new_state: list[list[int]] = copy.deepcopy(self.state)
            new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]

            self.children.append(GraphNode(self, new_state, self.steps + 1))

    def __lt__(self, other: "GraphNode"):
        return self.approximated_cost < other.approximated_cost

    def __eq__(self, other: object):
        if not isinstance(other, GraphNode):
            return NotImplemented
        return self.state == other.state


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target: str = "123450"
        early_exit: list[list[int]] = [[1, 2, 3], [4, 5, 0]]

        if board == early_exit:
            return 0

        root: Optional["GraphNode"] = GraphNode(None, board, 0)

        visited: dict[str, int] = {}
        fringe = []
        heapq.heappush(fringe, root)

        while fringe:
            current_node: Optional["GraphNode"] = heapq.heappop(fringe)

            if (
                current_node.id in visited
                and current_node.steps > visited[current_node.id]
            ):
                continue

            visited[current_node.id] = current_node.steps

            if current_node.id == target:
                return current_node.steps

            current_node.expand()

            for child in current_node.children:
                if child.id not in visited:
                    heapq.heappush(fringe, child)

        return -1
