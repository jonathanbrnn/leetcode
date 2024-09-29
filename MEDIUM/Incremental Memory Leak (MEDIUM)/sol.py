class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        time = 1

        while True:
            if time > memory1 and time > memory2:
                return [time, memory1, memory2]
            elif memory1 >= memory2:
                memory1 -= time
            else:
                memory2 -= time
            time += 1
