class Queue():
    def __init__(self):
            self.s1 = []
            self.s2 = []

    def push(self, x):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self):
        return self.s1.pop()

    def peek(self):
        return self.s1[-1]

    def empty(self):
        return not self.s1

    def printQueue(self):
        print(self.s1)
        print(self.s2)

stack1 = Queue()
arr1 = [1,2,3,4,5,6,7]
for num in arr1:
    stack1.push(num)
    stack1.printQueue()
# Test
