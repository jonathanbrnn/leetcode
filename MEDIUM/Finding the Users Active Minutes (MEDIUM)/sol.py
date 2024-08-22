class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        users = {}

        for user in logs:
            if user[0] not in users:
                users[user[0]] = set()
            users[user[0]].add(user[1])

        res = [0] * k

        for val in users.values():
            res[len(val) - 1] = res[len(val) - 1] + 1

        return res
