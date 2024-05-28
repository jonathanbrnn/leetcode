class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        sol = [""]

        for digit in digits:
            temp = []
            for s in sol:
                for letter in mapping[int(digit)]:
                    temp.append(s + letter)
            sol = temp

        return sol
