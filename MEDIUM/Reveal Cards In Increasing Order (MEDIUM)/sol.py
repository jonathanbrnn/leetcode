from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: list[int]):
        deque_cards = deque()
        deck.sort(reverse = True)
        for card in deck:
            if deque_cards:
                deque_cards.appendleft(deque_cards.pop())
            deque_cards.appendleft(card)

        return deque_cards






deck = [17,13,11,2,3,5,7]
print(Solution().deckRevealedIncreasing(deck))
