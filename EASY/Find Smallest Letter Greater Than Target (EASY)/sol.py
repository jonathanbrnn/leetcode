class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        target = ord(target)

        for let in letters:
            if ord(let) > target:
                return let

        return letters[0]
