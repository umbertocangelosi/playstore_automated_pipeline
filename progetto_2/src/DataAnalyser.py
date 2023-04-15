import pandas as pd
import numpy as np

from afinn import Afinn

afn = Afinn()

class DataAnalyser:
    
    def __init__(self):
        pass

    def assign_sentiment (self, dataframe, data_reviews):
        dataframe.name = 'Google Database'
        print(f'\nAssigning sentiment to {dataframe.name}...\n')
        data_reviews['score'] = data_reviews['translated_review'].apply(afn.score)
        app_score = data_reviews.groupby(by='app').agg({'score':'mean'}).reset_index()
        dataframe = pd.merge(dataframe, app_score, how='left', on='app')
        dataframe = dataframe.dropna(subset='score')
        dataframe = dataframe[['app','score']]
        dataframe.name = 'Google Database'
        print(f'\nSentiment has been assigned to {dataframe.name}!\n')
        return dataframe