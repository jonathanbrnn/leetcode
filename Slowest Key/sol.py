class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        duration = releaseTimes[0]
        res = keysPressed[0]
        for i in range(1, len(releaseTimes)):
            if releaseTimes[i] - releaseTimes[i - 1] > duration:
                duration = releaseTimes[i] - releaseTimes[i - 1]
                res = keysPressed[i]
            elif releaseTimes[i] - releaseTimes[i - 1] == duration and ord(res) < ord(keysPressed[i]):
                duration = releaseTimes[i] - releaseTimes[i - 1]
                res = keysPressed[i]

        return res
