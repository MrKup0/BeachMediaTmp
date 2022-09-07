class Tweet:
    def __init__(self, id, url, impressions, engagement, erate, retweet, replies, likes, urlClicks):
        self.id = id
        self.url = url
        self.impressions = impressions
        self.engagement = engagement
        self.erate = erate
        self.retweets = retweet
        self.replies = replies
        self.likes = likes
        self.urlClicks = urlClicks

    def getID(self):
        return self.id

    def getURL(self):
        return self.url

    def getImps(self):
        return self.impressions

    def getEngage(self):
        return self.engagement

    def getERate(self):
        return self.erate

    def getRetweets(self):
        return self.retweets

    def getReplies(self):
        return self.replies

    def getLikes(self):
        return self.likes

    def getURLClicks(self):
        return self.urlClicks


class TweetCollection:
    def __init__(self):
        self.mainData: list = []
        self.n = 0

    def getMax(self) -> int:
        return self.n

    def addTweet(self, tweet: Tweet):
        self.mainData.append(tweet)
        self.n += 1

    def getTweet(self, i) -> Tweet:
        return self.mainData[i]
