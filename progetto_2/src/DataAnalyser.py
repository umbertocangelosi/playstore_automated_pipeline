import pandas as pd
import numpy as np
from afinn import Afinn
afn = Afinn()
import itertools

class DataAnalyser:
    
    def __init__(self):
        pass

    def assign_sentiment (self, dataframe, data_reviews):
        # negative = pd.read_excel('./progetto_2/data/raw/n.xlsx')
        # negative = negative.values.tolist()
        # positive = pd.read_excel('./progetto_2/data/raw/p.xlsx')
        # positive = positive.values.tolist()
        # words_p = list(itertools.chain.from_iterable(positive))
        # words_n = list(itertools.chain.from_iterable(negative))
        # sentiment_words = words_n + words_p

        data_reviews['Score'] = data_reviews['Translated_Review'].apply(afn.score)
        app_score = data_reviews.groupby(by='App').agg({'Score':'mean'}).reset_index()
        dataframe = pd.merge(dataframe, app_score, how='left', on='App')
        return dataframe