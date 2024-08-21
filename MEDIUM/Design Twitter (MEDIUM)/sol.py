import heapq

class Tweet:
    def __init__(self, tweetId: int, time: int):
        self.tweetId = tweetId
        self.time = time

class User:
    def __init__(self, userId: int) -> None:
        self.userId = userId
        self.tweets = []
        self.following = set()

    def postTweet(self, tweetId: int, time: int) -> None:
        self.tweets.append(Tweet(tweetId, time))

    def follow(self, followeeId: int) -> None:
        self.following.add(followeeId)

    def unfollow(self, followeeId: int) -> None:
        if followeeId in self.following:
            self.following.remove(followeeId)

class Twitter:
    def __init__(self):
        self.users = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = User(userId)
        self.users[userId].postTweet(tweetId, self.time)
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []

        min_heap = []
        user = self.users[userId]

        for tweet in user.tweets[-10:]:
            heapq.heappush(min_heap, (tweet.time, tweet.tweetId))

        for followeeId in user.following:
            if followeeId in self.users:
                for tweet in self.users[followeeId].tweets[-10:]:
                    heapq.heappush(min_heap, (tweet.time, tweet.tweetId))
                    if len(min_heap) > 10:
                        heapq.heappop(min_heap)

        return [heapq.heappop(min_heap)[1] for _ in range(len(min_heap))][::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)
        self.users[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            self.users[followerId].unfollow(followeeId)


obj = Twitter()
obj.postTweet(1,2)
print(obj.getNewsFeed(1))
obj.follow(1,2)
obj.postTweet(2, 5)
print(obj.getNewsFeed(1))
obj.postTweet(2, 10)
print(obj.getNewsFeed(1))
obj.follow(2,1)
obj.postTweet(1, 14)
obj.unfollow(2,1)
print(obj.getNewsFeed(2))
