class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date = date.split("-")
        res = []

        for i in date:
            res.append(bin(int(i)).replace("0b", ""))

        return "-".join(res)
