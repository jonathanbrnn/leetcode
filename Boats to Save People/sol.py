class Solution:
    def numRescueBoats(self, people: list, limit: int) -> int:
        boats = 0
        left = 0
        right = len(people) - 1

        people = sorted(people)

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1

        return boats


people = [3,2,2,1]
limit = 3
sol = Solution()
print(sol.numRescueBoats(people, limit))
