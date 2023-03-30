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
dc.clean_all(google_data)
di.save_file(google_data, "./progetto_2/data/output/cleaned_data/googleplaystore_cleaned.pkl")

negative = di.read_file('./progetto_2/data/raw/n.xlsx').values.tolist()
positive = di.read_file('./progetto_2/data/raw/p.xlsx').values.tolist()
google_reviews = di.read_file('./progetto_2/data/raw/googleplaystore_user_reviews.csv')


# PULIRE IL FILE DELLE REVIEWS
# SALVARE IL FILE DELLE REVIEWS PULITO
da.assign_sentiment(google_data, google_reviews)

google_sentiment_data = di.read_file('./progetto_2/data/output/analysis/google_scored.pkl')

# SE SI VUOLE OPERARE SUL FILE COL SENTIMENT BISOGNA RICHIAMARSELO COL DATA INGESTOR
