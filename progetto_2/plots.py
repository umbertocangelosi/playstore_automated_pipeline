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

google_data = di.read_file("./progetto_2/database/googleplaystore_cleaned.csv")

#dv.scatter_corr(google_data,'Rating','Reviews')

#1
#dv.top_high_installs(google_data)

#2
#dv.top_rating_by_cat(google_data)

#3
#dv.top_paid_cat(google_data)

#4
#dv.Plot_price_per_contentrating(google_data)



