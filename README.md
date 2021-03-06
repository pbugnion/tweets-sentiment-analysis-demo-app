
# Demo Plotly Dash application

Demo application demonstrating creating a very simple [Plotly
Dash](https://plot.ly/products/dash/) application. This application
was presented at [ODSC Europe](https://odsc.com/london) in September
2018.

![](screenshot.png)

## Running the application

To install the dependencies, run the following in the root directory:

```
pip install -r requirements.txt
python -c "import nltk ; nltk.download('vader_lexicon')"
```

To start the application, run the following in `app/`:

```
python app.py
```

This will open the application on port 8888. Navigate with your browser to:

```
http://localhost:8888
```

You can find sample CSVs to upload at:
- [larger dataset](http://fileshare.pascalbugnion.net/tweets-sentiment-analysis/all-tweets.csv): this contains about 18,000 tweets.
- [subsampled dataset](http://fileshare.pascalbugnion.net/tweets-sentiment-analysis/subsampled-tweets.csv): this contains about 15,00 tweets.



