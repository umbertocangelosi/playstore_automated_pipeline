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

di = DataIngestor()
dc = DataCleaner()
da = DataAnalyser()
dv = DataVisualizer()

google_data = di.read_file("./data/raw/googleplaystore.csv")
google_data = dc.clean_googledb(google_data)


'''qui ci sono diverse operazioni di cleaning importanti da mettere dentro il 
datacleaner per potere interagire senza errori con postgres'''
google_data=google_data.dropna(subset='Type')
google_reviews = di.read_file('./data/raw/googleplaystore_user_reviews.csv')
google_reviews = dc.clean_googlereviews(google_reviews)

'''idem con patatate ci sono diverse operazioni di cleaning importanti da mettere dentro il 
datacleaner per potere interagire senza errori con postgres'''
google_reviews=google_reviews.dropna()
google_reviews['translated_review'] = google_reviews['translated_review'].astype(str)
google_reviews=google_reviews[google_reviews['app'].isin(google_data['app'])]

#ora i dati dovrebbero essere pronti per la parte di caricamento nel database

#creo la connessione al database con psycopg2
conn = di.connect('postgres','postgres','almno','localhost','5432')

#creo le tabelle vuote tramite psycopg passando internamente le ddl
di.create_google(conn)
di.create_reviews(conn)

#creo una connessione al database compatibile con il metodo db.to_sql(), usando la libreria sqlalchemy
engine=di.create_engine('postgres','almno','localhost','5432','postgres')


#carico i dati dei dataframe dentro postgress, che fungera' ora da data warehouseb
di.load(google_data,'googleplaystore',engine,replace=True,conn=conn)
di.load(google_reviews,'google_reviews',engine,replace=True,conn=conn)