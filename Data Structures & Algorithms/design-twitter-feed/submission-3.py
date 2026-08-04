class Twitter:

    class Tweet:
        def __init__(self, tweetId, userId):
            self.tweetId = tweetId
            self.userId = userId
            self.next = None
    
    class User:
        def __init__(self, userId):
            self.userId = userId
            self.followers = {userId: True}

    def __init__(self):
        self.users = {}
        self.tweets = None

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = self.User(userId)
        tweet = self.Tweet(tweetId, userId)
        tweet.next = self.tweets
        self.tweets = tweet

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []
        head = self.tweets
        count = 0
        result = []
        followers = self.users[userId].followers
        while count < 10 and head:
            if head.userId in followers:
                count += 1
                result.append(head.tweetId)
            head = head.next
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = self.User(followerId)
        if followeeId not in self.users:
            self.users[followeeId] = self.User(followeeId)
        self.users[followerId].followers[followeeId] = True
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = self.User(followerId)
        if followeeId not in self.users:
            self.users[followeeId] = self.User(followeeId)
        if followerId == followeeId:
            return
        if followeeId in self.users[followerId].followers:
            del self.users[followerId].followers[followeeId]
