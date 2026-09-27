import heapq
from typing import List

class Twitter:
    #users: hashmap of form: userId: set(tweetids)
    #userfollowers: hashmap of form: followerid: set(followeeid)
    #heap to keep 10 most recent ids: min heap of form: (userId, timestamp)

    def __init__(self):
        self.users = {}
        self.userFollowers = {}
        self.posts = []
        heapq.heapify(self.posts)
        self.timestamp = 0

    
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users: 
            self.users[userId] = set([tweetId])
        else:
            self.users[userId].add(tweetId)
        #add to heap 
        heapq.heappush(self.posts,(-self.timestamp, userId, tweetId)) # to heapify sorted in timestamp order
        self.timestamp +=1 

    def getNewsFeed(self, userId: int) -> List[int]:
        #we need to check the userfollowers dictionary 
        #use the heap to get the first 10 (at most)
        #use the userfollowers dict to check if its valid
        #valid would mean: userId in heap is in userfollowers dictionary
        recentPosts = []
        followed = self.userFollowers.get(userId, set())
        followed = followed | {userId} 

        temp_heap = list(self.posts)   
        heapq.heapify(temp_heap)   

        while temp_heap and len(recentPosts) < 10:
            time, postUserId, tweetId = heapq.heappop(temp_heap)
            if postUserId in followed:
                recentPosts.append(tweetId)
        return recentPosts




    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userFollowers: 
            self.userFollowers[followerId] = set([followeeId])
        else:
            self.userFollowers[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userFollowers:
            self.userFollowers[followerId].discard(followeeId)
 
