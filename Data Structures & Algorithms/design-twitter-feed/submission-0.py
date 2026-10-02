from collections import defaultdict

class Twitter:
    # Tweets -> a stack
    # Users -> a dict with key: user_id and value: set of ids they follow
    def __init__(self):
        self.tweets = list()
        self.users = defaultdict(set)
        
    # Add to the news tweets stack
    # Time and Space: O(1)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    # Loop through the list from the end
    # Check if item x is in the user's followers set
    # If so, append to feed
    # Return feed (this is correct since latest item is at the start)
    # Time: O(n). Space: O(1)
    def getNewsFeed(self, userId: int) -> List[int]:
        i = len(self.tweets) - 1
        feed = list()
        following = self.users[userId]
        following.add(userId)

        while i >= 0 and len(feed) < 10:
            post = self.tweets[i]

            if post[0] in following:
                feed.append(post[1])
            
            i -= 1
        return feed
        
        
    # In the users hashmap, get the follower id and add followee to set
    # Time and Space: O(1)
    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)
        

    # In the users hashmap, get the follower id and remove followee to set
    # Time and Space: O(1)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)
