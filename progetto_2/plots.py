import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.axes as ax
import seaborn as sns
import numpy as np
from src.DataIngestor import DataIngestor
from src.DataCleaner import DataCleaner
from src.DataVisualizer import DataVisualizer

dc = DataCleaner()
di = DataIngestor()
dv = DataVisualizer()

scores_google = di.read_file('.\progetto_2\data\output\google_scored.pkl')
google = di.read_file('.\progetto_2\data\output\googleplaystore_cleaned.pkl')

#dv.scatter_corr(google_data,'Rating','Reviews')
# dv.top_smallest(google,library='sns',quantity=6)
# print('\nRiga19\n')
# dv.scatter_corr(google,'Rating','Reviews')
# print('\nRiga21\n')
# dv.top_paid(google,library='sns',quantity=6)
# print('\nRiga23\n')
# dv.top_apps(google,library='sns',quantity=10)
# print('\nRiga25\n')
# dv.top_categories(google,library='sns')
# print('\nRiga27\n')
# dv.top_paid_categories(google,library='sns')
# print('\nRiga29\n')
# dv.avg_price_users(google,library='sns')
# print('\nRiga31\n')
# dv.top_free_by_sentiment(scores_google,library='sns',quantity=6)
# print('\nRiga33\n')
# dv.worst_free_by_sentiment(scores_google,library='sns',quantity=6)
# print('\nRiga35\n')
# dv.worst_paid_by_sentiment(scores_google,library='sns',quantity=6)
# print('\nRiga37\n')
# dv.top_paid_by_sentiment(scores_google,library='sns',quantity=6)
# print('\nRiga39\n')
# dv.categories_by_sentiment(scores_google,library='sns')
# print('\nRiga41\n')
# dv.top_by_sentiment(scores_google,library='sns',quantity=6)
# print('\nRiga43\n')
# dv.top_by_sentiment(scores_google,column2='Rating', library='sns',quantity=6)
# dv.rating_vs_score(scores_google, quantity=6, worst_results=True)
# dv.scatter_corr(scores_google,'Score','Rating')



