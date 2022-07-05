import matplotlib.pyplot as plt
from wordcloud import WordCloud


def selection_positive_sentiment(df):
    return df[df['sentiment_category'] == 'positive']


def selection_negative_sentiment(df):
    return df[df['sentiment_category'] == 'negative']


def show_word_cloud(df, sentiment):
    wordcloud = WordCloud(max_font_size=50, max_words=500, background_color="white").generate(
        str(df['Text']))
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    if sentiment == 'positive':
        plt.savefig("positive_words.png")
    else:
        plt.savefig("negative_words.png")
    plt.show()

