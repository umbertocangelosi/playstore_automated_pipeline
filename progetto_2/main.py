import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from src.DataIngestor import DataIngestor
di = DataIngestor()
from src.DataCleaner import DataCleaner
dc = DataCleaner()
from src.DataVisualizer import DataVisualizer
dv = DataVisualizer()
from src.DataAnalyser import DataAnalyser
da = DataAnalyser()

google_data = di.read_file("./progetto_2/data/raw/googleplaystore.csv")
google_data = dc.clean_googledb(google_data)
di.save_file(google_data, "./progetto_2/data/output/cleaned_data/googleplaystore_cleaned.pkl")

negative = di.read_file('./progetto_2/data/raw/n.xlsx').values.tolist()
positive = di.read_file('./progetto_2/data/raw/p.xlsx').values.tolist()
sentiment_words = dc.clean_sentiment_list(positive,negative)

google_reviews = di.read_file('./progetto_2/data/raw/googleplaystore_user_reviews.csv')
google_reviews = dc.clean_googlereviews(google_reviews)
google_reviews = dc.replace_common_strings(google_reviews, 'Translated_Review', sentiment_words)
di.save_file(google_reviews, './progetto_2/data/output/cleaned_data/google_reviews.pkl')

da.assign_sentiment(google_data, google_reviews)
di.save_file(google_data, './progetto_2/data/output/analysis/google_scored.pkl')
print ('\ngoogle_scored.pkl has been stored successfully\n')
google_sentiment_data = di.read_file('./progetto_2/data/output/analysis/google_scored.pkl')

