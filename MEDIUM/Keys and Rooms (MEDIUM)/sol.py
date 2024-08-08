class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [0] * n
        keys = rooms[0]

        while keys:
            for i in range(len(rooms[keys[0]])):
                if rooms[keys[0]][i] and visited[keys[0]] == 0:
                    keys.append(rooms[keys[0]][i])
            visited[keys[0]] = 1
            keys.pop(0)

        return sum(visited) == n - 1
