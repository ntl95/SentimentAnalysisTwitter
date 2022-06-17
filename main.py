import scraping_and_store as scr
import analyze_tweets_sentiment as sentiment
import pandas as pd
import data_chart_visualization as chart


def main():
    scr.create_csv()
    df = pd.read_csv('5g.csv')
    sentiment.create_csv_with_sentiment(df)

    df2 = pd.read_csv('final.csv')
    chart.data_visualization(df2)


if __name__ == '__main__':
    main()
