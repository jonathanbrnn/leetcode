class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        wordRes = []
        indexRes = 10 ** 4
        for i, word in enumerate(list1):
            if word in list2:
                curr = list2.index(word) + i
                if curr < indexRes:
                    indexRes = curr
                    wordRes = [word]
                elif curr == indexRes:
                    wordRes.append(word)
        return wordRes
