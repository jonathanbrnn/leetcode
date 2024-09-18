class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        if self.events == []:
            self.events.append(start)
            self.events.append(end)
            return True
        else:
            if start >= self.events[-1][1]:
                self.events.append(start)
                self.events.append(end)
                return True
            elif end <= self.events[0]:
                self.events.append(start)
                self.events.append(end)
                self.events.sort()
                return True
            for i in range(len(self.events) - 1):
                if self.events[i] <= start < self.events[i + 1] and self.events[i + 1] >= end:
                    self.events.append(start)
                    self.events.append(end)
                    self.events.sort()
                    return True
            return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
