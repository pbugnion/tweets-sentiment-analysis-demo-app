
from nltk.tokenize.casual import TweetTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class TweetSentimentAnalyzer:

    def __init__(self):
        self.tokenizer = TweetTokenizer(reduce_len=True, strip_handles=True)
        self.analyzer = SentimentIntensityAnalyzer()

    def get_sentiment(self, text):
        cleaned_tweet = ' '.join(self.tokenizer.tokenize(text))
        return self.analyzer.polarity_scores(cleaned_tweet)['compound']
