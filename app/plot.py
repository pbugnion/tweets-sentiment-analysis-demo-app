
import plotly.graph_objs as go


def create_plot_data(tweets_df):
    plot_data = []
    tweets_grouped_by_handle = tweets_df.groupby('handle')
    for handle, tweets_for_handle in tweets_grouped_by_handle:
        mean = tweets_for_handle['sentiment'].resample('H').mean()
        plot_data.append(go.Scatter(x=mean.index, y=mean, name=handle))
    return plot_data
