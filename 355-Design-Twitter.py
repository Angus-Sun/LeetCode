class Twitter:

    def __init__(self):
        self.follower_map = defaultdict(set)
        self.tweet_map = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((tweetId, self.count))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap, res = [], []
        self.follower_map[userId].add(userId)

        for followeeId in self.follower_map[userId]:
            index = len(self.tweet_map[followeeId])-1
            if index >= 0:
                tweetId, time = self.tweet_map[followeeId][index]
                maxHeap.append((time, followeeId, tweetId, index-1))
        heapq.heapify(maxHeap)

        while maxHeap and len(res) < 10:
            time, followeeId, tweetId, index = heapq.heappop(maxHeap)
            res.append(tweetId)
            if index >= 0:
                tweetId, time = self.tweet_map[followeeId][index]
                heapq.heappush(maxHeap, (time, followeeId, tweetId, index-1)) 
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follower_map:
            self.follower_map[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)