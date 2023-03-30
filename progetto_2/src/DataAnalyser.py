import pandas as pd
import numpy as np
from afinn import Afinn as afn
from src.DataIngestor import DataIngestor


class DataAnalyser:
    
    def __init__(self):
        pass

    def analysis (self, dataframe):
        import itertools
        negative = pd.read_excel('./progetto_2/data/raw/n.xlsx')
        negative = negative.values.tolist()
        positive = pd.read_excel('./progetto_2/data/raw/p.xlsx')
        positive = positive.values.tolist()        
        lista_appiattita_p = list(itertools.chain.from_iterable(positive))
        lista_appiattita_n = list(itertools.chain.from_iterable(negative))
        lista = lista_appiattita_n + lista_appiattita_p
        def replace_common_strings(dataframe, col_name, string_list):
            dataframe[col_name] = dataframe[col_name].apply(lambda x: " ".join([string for string in str(x).split() if string in string_list]))
            return dataframe
        replace_common_strings(dataframe, 'Translated_Review', lista)
        # creating Score column for each review
        dataframe['Score'] = dataframe['Translated_Review'].apply(afn.score)
        # grouping reviews dataframe by App name and calculating ['Score'] mean
        app_score = dataframe.groupby(by='App').agg({'Score':'mean'}).reset_index()
        # merging ['Score'] mean to primary google dataset
        dataframe = pd.merge(dataframe, app_score, how='left', on='App')
        return dataframe