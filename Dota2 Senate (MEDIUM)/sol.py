# DISCLAIMER: This is a HORRIBLE solution. I just wanted to get it done and over with. No I won't be coming back to this, yes I am ashamed of this solution. I am sorry.
# I will be taking a closer look at deques and queues and I hope the next time I come across a problem like this I will be able to solve it in a more elegant way.

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire_count = senate.count("D")
        radiant_count = senate.count("R")

        senate = [x for x in senate]

        while True:
            if dire_count <= 0:
                return "Radiant"
            if radiant_count <= 0:
                return "Dire"

            index = -1
            if senate[0] == "D":
                radiant_count -= 1
                for i in range(len(senate)):
                    if senate[i] == "R":
                        index = i
                        break
                senate.pop(index)
                senate.append(senate.pop(0))
            else:
                dire_count -= 1
                for i in range(len(senate)):
                    if senate[i] == "D":
                        index = i
                        break
                senate.pop(index)
                senate.append(senate.pop(0))
