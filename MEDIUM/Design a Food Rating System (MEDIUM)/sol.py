class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.c = defaultdict(list)
        self.f = {}

        for cuisine, food, rating in zip(cuisines, foods, ratings):
            self.f[food] = (rating, cuisine)
            heapq.heappush(self.c[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        old_rating, cuisine = self.f[food]
        self.f[food] = (newRating, cuisine)
        heapq.heappush(self.c[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while self.c[cuisine]:
            rating, food = self.c[cuisine][0]
            if -rating == self.f[food][0]:
                return food
            heapq.heappop(self.c[cuisine])
