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

google_data = di.read_file("./progetto_2/data/raw/googleplaystore.csv")
dc.clean_googledb(google_data)

# CARICARE IL FILE DELLE REVIEWS IN CSV
google_reviews = di.read_file('./progetto_2/data/raw/googleplaystore_user_reviews.csv')
# PULIRE IL FILE DELLE REVIEWS
dc.clean_googlereview(google_reviews)