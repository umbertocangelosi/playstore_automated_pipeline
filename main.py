import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import psycopg2
from sqlalchemy import create_engine

from src.DataIngestor import DataIngestor
from src.DataCleaner import DataCleaner
from src.DataVisualizer import DataVisualizer
from src.DataAnalyser import DataAnalyser
from src.DbHandler import DbHandler

di = DataIngestor()
dc = DataCleaner()
da = DataAnalyser()
dv = DataVisualizer()
dbh = DbHandler('postgresql://aljfqalc:eCoshU-kD2hhOB0mJg014ID64-m2e6Er@flora.db.elephantsql.com/aljfqalc')

# import, clean, and export google_data can be done in one function
google_data = di.read_file("./progetto_2/data/raw/googleplaystore.csv")
google_data = dc.clean_google(google_data)

google_reviews = di.read_file('./progetto_2/data/raw/googleplaystore_user_reviews.csv')
google_reviews = dc.clean_google_reviews(google_reviews, google_data)

dbh.create_table_google()
dbh.create_table_reviews()


#carico i dati dei dataframe dentro postgress, che fungera' ora da data warehouseb
di.to_cloud(google_data, 'google_play_store')
di.to_cloud(google_reviews, 'google_reviews')

#google_data = da.assign_sentiment(google_data, google_reviews)

