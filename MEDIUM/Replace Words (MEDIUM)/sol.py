class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split()
        dictionary = sorted(dictionary)

        res = []

        for word in sentence:
            curr = True
            for root in dictionary:
                if word[:len(root)] == root:
                    res.append(root)
                    curr = False
                    break
            if curr:
                res.append(word)

        return " ".join(res)
