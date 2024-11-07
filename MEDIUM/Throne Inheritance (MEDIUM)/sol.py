from collections import defaultdict
from typing import List

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.children = defaultdict(list)
        self.deceased = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deceased.add(name)

    def getInheritanceOrder(self) -> List[str]:
        def dfs(person):
            if person not in self.deceased:
                order.append(person)
            for child in self.children[person]:
                dfs(child)

        order = []
        dfs(self.king)
        return order
