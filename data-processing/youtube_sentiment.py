import numpy as np
import pandas as pd

def get_youtube_sentiment(video_stats_df):
    # Write your code here.
    video_stats_df['total'] =  video_stats_df['likes'] + video_stats_df['dislikes']
    video_stats_df['percent_of_likes'] = video_stats_df['likes']/video_stats_df['total']
    grp = pd.DataFrame(video_stats_df.groupby('category_id')['percent_of_likes'].mean())
    grp.columns = ['mean_sentiment']
    grp.sort_values('mean_sentiment', inplace=True, ascending=False)
    return grp