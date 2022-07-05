import plotly.graph_objs as go


def data_visualization(df):
    neg = df[df['sentiment_category'] == 'negative']
    neg = neg.groupby(['Datetime'], as_index=False).count()

    pos = df[df['sentiment_category'] == 'positive']
    pos = pos.groupby(['Datetime'], as_index=False).count()

    pos = pos[['Datetime', 'Tweet_ID']]
    neg = neg[['Datetime', 'Tweet_ID']]

    fig = go.Figure()
    for col in pos.columns:
        fig.add_trace(go.Scatter(x=pos['Datetime'], y=pos['Tweet_ID'],
                                 name=col,
                                 mode='markers+lines',
                                 line=dict(shape='linear'),
                                 connectgaps=True,
                                 line_color='green'
                                 )
                      )

    for col in neg.columns:
        fig.add_trace(go.Scatter(x=neg['Datetime'], y=neg['Tweet_ID'],
                                 name=col,
                                 mode='markers+lines',
                                 line=dict(shape='linear'),
                                 connectgaps=True,
                                 line_color='red'
                                 )
                      )

    fig.show()
