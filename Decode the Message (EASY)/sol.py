class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dic = {" ":" "}
        j = 0
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        res = ""

        for char in key:
            if char not in dic:
                dic[char] = alphabet[j]
                j += 1

        for i in range(len(message)):
            res += dic[message[i]]

        return res
