
import base64
import io

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

import pandas as pd

from sentiment import TweetSentimentAnalyzer
from plot import create_plot_data

analyzer = TweetSentimentAnalyzer()

app = dash.Dash()

app.layout = html.Main(
    children=[
        html.H1('Sentiment analyzer', className='mt-5'),
        dcc.Upload(
            'Drag CSV here',
            className='sentiment-app-file-upload',
            id='sentiment-app-file-upload'
        ),
        html.Div(
            children=[],
            id='sentiment-app-output-div'
        )
    ],
    className='container'
)


def parse_upload(uploaded_contents):
    _, file_contents = uploaded_contents.split(',')
    parsed_contents = base64.b64decode(file_contents).decode('utf-8')
    df = pd.read_csv(
        io.StringIO(parsed_contents),
        parse_dates=True,
        index_col=0
    )
    return df


def add_sentiment(tweets_df):
    tweets_df['sentiment'] = [
        analyzer.get_sentiment(text)
        for text in tweets_df['text']
    ]


@app.callback(
    Output('sentiment-app-output-div', 'children'),
    [Input('sentiment-app-file-upload', 'contents')]
)
def on_upload(uploaded_contents):
    if uploaded_contents is not None:
        df = parse_upload(uploaded_contents)
        add_sentiment(df)
        plot_data = create_plot_data(df)
        return [
            dcc.Graph(
                figure={'data': plot_data},
                id='sentiment-app-output-graph'
            )
        ]


if __name__ == '__main__':
    print('Starting application...')
    app.run_server(debug=True, port=8888)
