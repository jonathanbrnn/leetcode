class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer = []
        winners = []
        loosers = []
        answer0 = []
        answer1 = []
        for match in matches:
            winners.append(match[0])
            loosers.append(match[1])
        for winner in winners:
            if winner not in loosers and winner not in answer0:
                answer0.append(winner)
        for looser in loosers:
            if loosers.count(looser) == 1:
                answer1.append(looser)

        answer0.sort()
        answer1.sort()

        answer.append(answer0)
        answer.append(answer1)
        return answer
