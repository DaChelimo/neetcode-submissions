from collections import defaultdict
from heapq import heapify, heappop, heappush

class Twitter:

    # Decrementing count moves further into the future ie count = -10 is more recent than count = 0
    count = 0

    # Tweets: Hashmap of key (userId) -> value (list of (timestamp, tweetId))
    # Users: HashMap of key(userId) -> value(set of followers)
    def __init__(self):
        self.tweets = defaultdict(list)
        self.users = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((Twitter.count, tweetId))
        Twitter.count -= 1
        

    # Add the user's id to the following list
    # Loop through users follows, get their most recent post, add to our heap 
    # Loop through heap while results < 10:
    #   1. Get the lowest value
    #   2. For that value, get the previous post and add to the heap 
    #           -> our heap should store the prev index, which user
    # Return results
    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []

        following = self.users[userId]
        following.add(userId)

        for ID in following:
            index = len(self.tweets[ID]) - 1

            if index >= 0:
                (count, tweetId) = self.tweets[ID][index]
                minHeap.append((count, tweetId, ID, index))
        
        heapify(minHeap)

        results = []

        while minHeap and len(results) < 10:
            (count, tweetId, ID, index) = heappop(minHeap)

            results.append(tweetId)

            if index > 0: # Get the next element and add to heap
                newIndex = index - 1
                (newCount, newTweetID) = self.tweets[ID][newIndex]
                heappush(minHeap, (newCount, newTweetID, ID, newIndex))

        return results

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)
        
