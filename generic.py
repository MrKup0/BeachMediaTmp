import article
import readers
import tweets

# better way to handle this, look into refactoring
class dataCollection:
    def __init__(self, type: str):
        self.struct: list = []
        self.n: int = 0
        if type is "twitter" or "web" or "article":
            self.internalType = type
        else:
            self.internalType = None

    # remove?
    def validate(self) -> bool:
        return self.internalType is not None

    def import(self, fileName: str):

        if not self.validate():
            return

        if self.internalType is "twitter":
            self.struct = readers.read_tweet_csv_file(fileName)
        else:
            self.struct = readers.read_article_data(fileName)

        for value in self.struct:
            self.n += 1

    def getData(self, pos: int):
        if 0 <= pos < self.n:
            return self.struct[pos]
        else:
            return None

    def getType(self):
        return seld.internalType
