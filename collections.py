# main collections file
import numpy as np
from tweets import Tweet
from article import Article
import csv


class DataCollection:
    def __init__(self, type: str):
        self.struct: np.array = np.array([])
        self.n: int = 0
        if type is "twitter" or "web" or "article":
            self.internalType = type
        else:
            self.internalType = None

    # remove?
    def validate(self) -> bool:
        return self.internalType is not None

    def getData(self, pos: int):
        if 0 <= pos < self.n:
            return self.struct[pos]
        else:
            return None

    def addData(self, data):
        self.struct = np.concatenate((self.struct, data))
        self.n += 1

    def getType(self) -> str:
        return self.internalType

    def getMax(self) -> int:
        return self.n

    def aBadFunction(self) -> np.array:
        return self.struct

    def getSpecific(self, val: str, pos: int):
        return None


class TweetCollection(DataCollection):
    def __init__(self, type: str, filename: str):
        super().__init__(type)

        with open(filename, "r") as file:
            first_line = True

            for line in file:
                if first_line:
                    first_line = False
                    continue

                id = str(line[0])
                # id = float(line[0])
                url = str(line[1])
                imps = float(line[4])
                eng = float(line[5])
                er = float(line[6])
                retweet = float(line[7])
                reply = float(line[8])
                like = float(line[9])
                urlC = float(line[11])

                reading: np.array = np.array([Tweet(id, url, imps, eng, er, retweet, like, reply, urlC)])
                self.addData(reading)

    def getSpecific(self, val: str, pos: int):
        # i hope this works!
        tmp: Tweet = self.getData(pos)
        match val:
            case "id":
                return tmp.getID()
            case "url":
                return tmp.getURL()
            case "impressions":
                return tmp.getImps()
            case "engagement":
                return tmp.getEngage()
            case "erate":
                return tmp.getERate()
            case "retweets":
                return tmp.getRetweets()
            case "replies":
                return tmp.getReplies()
            case "likes":
                return tmp.getLikes()
            case "urlclicks":
                return tmp.getURLClicks()
            case _:
                return None


class ArticleCollection(DataCollection):
    def __init__(self, type: str, filename: str, isD49: bool):
        super().__init__(type)

        with open(filename, "r") as file:
            first_line = True

            for line in file:
                if first_line:
                    first_line = False
                    continue

                split = line.split(",")
                url = str(split[0])
                views = float(split[1])
                uViews = float(split[2])
                reading = Article(url, views, uViews)
                if isD49:
                    reading.isD49()
                self.addData(reading)

    def getSpecific(self, val: str, pos: int):
        tmp: Article = self.getData(pos)
        match val:
            case "views":
                return tmp.getViews()
            case "uviews" | "uViews" | "unique":
                return tmp.getUniqueViews()
            case "url":
                return tmp.getURL()
            case _:
                return None
