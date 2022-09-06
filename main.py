# Test pycode for data
# input()
import article
import readers
import tweets

# better way to handle this, look into refactoring
class genericDataStructure:
    def __init__(self, type: str):
        self.internalType = type
        if type is "twitter":
            self.struct = tweets.TweetCollection()
        elif type is "web" or "article":
            self.struct = article.ArticleCollection()
        else:
            self.struct = None

    # check this behaves as intended
    def validate(self) -> bool:
        return self.internalType is not None

    def import(self, fileName: str):

        if not self.validate():
            return None

        if self.internalType is "twitter":
            self.struct = readers.read_tweet_csv_file(fileName)
        else:
            self.struct = readers.read_article_data(fileName)

    def use(self):
        return self.struct

# god I love switch cases
def switch(arg: str):
    if arg is ""

if __name__ == '__main__':
    # outline
    case = input("Which kind of file?:")

    mainData = genericDataStructure(case)

    fileName = input("Enter file name with suffix:")
    mainData.import(fileName)
