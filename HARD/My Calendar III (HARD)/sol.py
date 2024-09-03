class MyCalendarThree:
    def __init__(self):
        self.dic = defaultdict(int)
        self.events = []

    def book(self, startTime: int, endTime: int) -> int:
        self.dic[startTime] += 1
        self.dic[endTime] -= 1

        self.events.append((startTime, 1))
        self.events.append((endTime, -1))

        self.events.sort()

        max_k = 0
        current_k = 0

        for time, effect in self.events:
            current_k += effect
            max_k = max(max_k, current_k)

        return max_k

# Usage
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
