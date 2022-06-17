import nltk
import re
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
nltk.download('words')
words = set(nltk.corpus.words.words())


def cleaner(tweet):
    tweet = re.sub("@[A-Za-z0-9]+", "", tweet)  # Remove @ sign
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet)  # Remove http links
    tweet = " ".join(tweet.split())
    tweet = tweet.replace("#", "").replace("_", " ")  # Remove hashtag sign but keep the text
    tweet = " ".join(w for w in nltk.wordpunct_tokenize(tweet)
                     if w.lower() in words or not w.isalpha())
    return tweet


def list_values_sentiment(df):
    print("I'm analyzing the sentences...")
    sid = SentimentIntensityAnalyzer()
    df['tweet_clean'] = df['Text'].apply(cleaner)
    list1 = []
    for i in df['tweet_clean']:
        score = (sid.polarity_scores(str(i)))
        list1.append(score['compound'])
    return list1


def sentiment_category(sentiment):
    label = ''
    if sentiment > 0:
        label = 'positive'
    elif sentiment == 0:
        label = 'neutral'
    else:
        label = 'negative'
    return label


def create_csv_with_sentiment(df):
    listValuesSentiment = list_values_sentiment(df)
    df['sentiment'] = pd.Series(listValuesSentiment)
    df['sentiment_category'] = df['sentiment'].apply(sentiment_category)
    df = df[['Text', 'Datetime', 'Tweet_ID', 'sentiment', 'sentiment_category']]
    df.to_csv('final.csv')
