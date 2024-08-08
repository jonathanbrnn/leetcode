class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        counts = [0, 0]
        for student in students:
            counts[student] += 1

        remaining = len(sandwiches)
        for sandwich in sandwiches:
            if counts[sandwich] == 0:
                break
            if remaining == 0:
                break
            counts[sandwich] -= 1
            remaining -= 1

        return remaining


students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
print(Solution().countStudents(students, sandwiches))
