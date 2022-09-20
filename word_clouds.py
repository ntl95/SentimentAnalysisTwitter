import matplotlib.pyplot as plt
from wordcloud import WordCloud


def show_word_cloud(df):
    wordcloud = WordCloud(max_font_size=50, max_words=500, background_color="white").generate(
        str(df['Text']))
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig("words.png")
    plt.show()


'''
def selection_positive_sentiment(df):
    return df[df['sentiment_category'] == 'positive']


def selection_negative_sentiment(df):
    return df[df['sentiment_category'] == 'negative']
'''
