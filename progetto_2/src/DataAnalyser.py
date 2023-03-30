import pandas as pd
import numpy as np
from afinn import Afinn
from src.DataIngestor import DataIngestor
di = DataIngestor()
afn = Afinn()
import itertools

class DataAnalyser:
    
    def __init__(self):
        pass

    def assign_sentiment (self, dataframe, data_reviews):
        negative = pd.read_excel('./progetto_2/data/raw/n.xlsx')
        negative = negative.values.tolist()
        positive = pd.read_excel('./progetto_2/data/raw/p.xlsx')
        positive = positive.values.tolist()
        words_p = list(itertools.chain.from_iterable(positive))
        words_n = list(itertools.chain.from_iterable(negative))
        sentiment_words = words_n + words_p
        def replace_common_strings(dataframe, col_name, string_list):
            dataframe[col_name] = dataframe[col_name].apply(lambda x: " ".join([string for string in str(x).split() if string in string_list]))
            return dataframe
        replace_common_strings(data_reviews, 'Translated_Review', sentiment_words)
        data_reviews['Score'] = data_reviews['Translated_Review'].apply(afn.score)
        app_score = data_reviews.groupby(by='App').agg({'Score':'mean'}).reset_index()
        dataframe = pd.merge(dataframe, app_score, how='left', on='App')
        di.save_file(dataframe, './progetto_2/data/output/analysis/google_scored.pkl')
        print ('\ngoogle_scored.pkl has been stored successfully\n')