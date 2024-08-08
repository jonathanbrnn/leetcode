from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        res = []
        curr = ""
        n = 0
        for char in searchWord:
            curr += char
            n += 1
            to_append = []
            t = 0
            for product in products:
                if curr == product[:n]:
                    to_append.append(product)
                    t += 1
                if t >= 3:
                    break
            res.append(to_append)
        return res


print(Solution().suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))
