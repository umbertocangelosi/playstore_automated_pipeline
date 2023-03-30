import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from src.DataIngestor import DataIngestor
from src.DataCleaner import DataCleaner
from src.DataVisualizer import DataVisualizer

dc = DataCleaner()
di = DataIngestor()
dv = DataVisualizer()
#sns.set()
google_data = di.read_file("./progetto_2/data/output/cleaned_data/googleplaystore_cleaned.csv")
google_sentiment = di.read_file(r'.\progetto_2\database\googlevis.csv')
#dv.scatter_corr(google_data,'Rating','Reviews')

#1
#dv.top_high_installs(google_data)

#2
#dv.top_rating_by_cat(google_data)

#3
#dv.top_paid_cat(google_data)

#4
#dv.Plot_price_per_contentrating(google_data)

# Umberto plots

dv.global_by_sentiment(google_sentiment)


