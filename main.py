import scraping_and_store as scr
import analyze_tweets_sentiment as sentiment
import pandas as pd
import data_chart_visualization as chart
import word_clouds as wdc


def main():
    scr.create_csv()
    df = pd.read_csv('5g.csv')
    sentiment.create_csv_with_sentiment(df)

    df2 = pd.read_csv('final.csv')
    chart.data_visualization(df2)
    df_positive = wdc.selection_positive_sentiment(df2)
    df_negative = wdc.selection_negative_sentiment(df2)
    wdc.show_word_cloud(df_positive, 'positive')
    wdc.show_word_cloud(df_negative, 'negative')


if __name__ == '__main__':
    main()
