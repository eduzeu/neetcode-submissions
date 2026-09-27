import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.users = defaultdict(list)  # userId -> list of [timestamp, tweetId]
        self.userFollowers = defaultdict(set)  # followerId -> set of followeeIds
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].append([self.timestamp, tweetId])
        self.timestamp -= 1  # newer tweets get smaller (more negative) timestamp for max-heap behavior

    def getNewsFeed(self, userId: int) -> List[int]:
        recentPosts = []
        minHeap = []

        # Make sure user follows themselves
        self.userFollowers[userId].add(userId)

        for followeeId in self.userFollowers[userId]:
            if followeeId in self.users and self.users[followeeId]:
                index = len(self.users[followeeId]) - 1
                time, tweetId = self.users[followeeId][index]
                heapq.heappush(minHeap, [time, tweetId, followeeId, index - 1])

        while minHeap and len(recentPosts) < 10:
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            recentPosts.append(tweetId)
            if index >= 0:
                next_time, next_tweetId = self.users[followeeId][index]
                heapq.heappush(minHeap, [next_time, next_tweetId, followeeId, index - 1])

        return recentPosts

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.userFollowers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollowers[followerId]:
            self.userFollowers[followerId].remove(followeeId)
