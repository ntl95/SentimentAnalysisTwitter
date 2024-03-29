import pandas as pd
import snscrape.modules.twitter as sntwitter
import sys


def create_csv():
    maxTweets = sys.maxsize

    # Creating list to append tweet data to
    tweets_list = []
    source = "Twitter"

    # Using TwitterSearchScraper to scrape data
    for i, tweet in enumerate(
            sntwitter.TwitterSearchScraper('5g radiation since:2020-01-01 until:2020-12-31 lang:it').get_items()):
        if i > maxTweets:
            break
        print(i)
        tweets_list.append(
            [tweet.id, tweet.url, tweet.user.username, tweet.content, tweet.date.date(), source, tweet.retweetCount,
             tweet.likeCount, tweet.replyCount])

    tweets_df = pd.DataFrame(tweets_list, columns=['Tweet_ID', 'URL', "Account_Name", 'Text', 'Datetime', 'Source',
                                                   'Number_Retweets', 'Number_Likes', 'Number_Comments'])

    tweets_df.to_csv("5g.csv")
