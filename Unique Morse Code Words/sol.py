class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        res = set()
        alph = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        for word in words:
            curr = ""
            for char in word:
                curr += alph[ord(char) - 97]
            res.add(curr)

        return len(res)
