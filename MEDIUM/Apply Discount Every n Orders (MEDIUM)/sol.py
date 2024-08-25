class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = ((100 - discount) / 100)

        self.customer_count = 0
        self.catalog = {}

        for i, product in enumerate(products):
            self.catalog[product] = prices[i]

    def getBill(self, product: List[int], amount: List[int]) -> float:
        total = 0
        self.customer_count += 1

        for prod, am in zip(product, amount):
            total += self.catalog[prod] * am

        if self.customer_count == self.n:
            self.customer_count = 0
            return total * self.discount

        return total


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
