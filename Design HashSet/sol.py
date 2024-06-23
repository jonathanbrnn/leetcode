'''
Runtime + Memory [717ms, 21.1mb]
class MyHashSet:

    def __init__(self):
        self.hashSet = []

    def add(self, key: int) -> None:
        if key not in self.hashSet:
            self.hashSet.append(key)

    def remove(self, key: int) -> None:
        if key in self.hashSet:
            i = self.hashSet.index(key)
            self.hashSet.pop(i)

    def contains(self, key: int) -> bool:
        return key in self.hashSet
'''

# Runtime + Memory [117ms, 21.53mb]
class MyHashSet:

    def __init__(self):
        self.hashSet = set()

    def add(self, key: int) -> None:
        self.hashSet.add(key)

    def remove(self, key: int) -> None:
        self.hashSet.discard(key)

    def contains(self, key: int) -> bool:
        return key in self.hashSet


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
