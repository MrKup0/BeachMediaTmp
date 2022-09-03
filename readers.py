import article
import tweets
import csv


# bastardized from CECS 323,
def read_article_data(filename: str, isD49: bool) -> article.ArticleCollection:
    with open(filename, "r") as file:
        all_readings = article.ArticleCollection()
        first_line = True

        for line in file:
            if first_line:
                first_line = False
                continue

            split = line.split(",")
            url = str(split[0])
            views = float(split[1])
            uViews = float(split[2])

            reading = article.Article(url, views, uViews)
            if isD49:
                reading.isD49()
            all_readings.addArticle(reading)

        return all_readings


def read_tweet_csv_file(filename: str) -> tweets.TweetCollection:
    with open(filename) as file:
        reader = csv.reader(file, delimiter=";")
        all_readings = tweets.TweetCollection()
        first_line = True

        for line in reader:
            if first_line:
                first_line = False
                continue
            id = float(line[0])
            url = str(line[1])
            imps = float(line[4])
            eng = float(line[5])
            er = float(line[6])
            retweet = float(line[7])
            reply = float(line[8])
            like = float(line[9])
            urlC = float(line[11])

            reading = tweets.Tweet(id, url, imps, eng, er, retweet, like, reply, urlC)
            all_readings.addTweet(reading)

    return all_readings
