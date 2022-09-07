# class template for each article

# use for any generic article
class Article:
    def __init__(self, url: str, views: float, uniqueViews: float):
        self.views = views
        self.uViews = uniqueViews
        self.url = url
        self.year = None
        self.month = None
        self.day = None
        self.title = None

    def isD49(self):
        x = self.url.split("/")
        self.year = float(x[1])
        self.month = float(x[2])
        self.day = float(x[3])
        self.title = float(x[4])

    def getViews(self):
        return self.views

    def getUniqueViews(self):
        return self.uViews

    def getTitle(self):
        return self.title

    def getYear(self):
        return self.year

    def getMonth(self):
        return self.month

    def getDay(self):
        return self.day

    def getTitle(self):
        if self.title is not None:
            return self.title
        else:
            return self.url

    # if you specifically need/know a None attribute use this
    # block to add these attributes
    def updateYear(self, y):
        self.year = y

    def updateMonth(self, m):
        self.month = m

    def updateDay(self, d):
        self.day = d

    def updateTitle(self, t: str):
        self.title = t


# custom list
class ArticleCollection:
    def __init__(self):
        self.mainData: list = []
        self.n: int = 0

    # add an article to the set
    def addArticle(self, article: Article):
        self.mainData.append(article)
        self.n += 1

    def numArticles(self) -> int:
        return self.n

    def getArticle(self, index: int) -> Article:
        return self.mainData[index]
