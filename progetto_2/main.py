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

# import, clean, and export google_data can be done in one function. need another class? is it worth?
google_data = di.read_file("./progetto_2/data/raw/googleplaystore.csv")
google_data = dc.clean_google(google_data)

google_reviews = di.read_file('./progetto_2/data/raw/googleplaystore_user_reviews.csv')
google_reviews = dc.clean_google_reviews(google_reviews)

#creo la connessione al database con psycopg2
pg2_connection = di.pg2_connect(dbname='postgres',
                                dbuser='postgres',
                                dbhost='localhost',
                                dbport='5432')

#creo le tabelle vuote tramite psycopg passando internamente le ddl
di.create_table_google(pg2_connection)
di.create_table_reviews(pg2_connection)

# creo una connessione al database compatibile con il metodo db.to_sql(), usando la libreria sqlalchemy
sqlalchemy_connection = di.sqlalchemy_connect(dbname='postgres',dbuser='postgres',dbhost='localhost',dbport='5432')

#carico i dati dei dataframe dentro postgress, che fungera' ora da data warehouseb
di.export_to_sql(google_data, 'googleplaystore', con=sqlalchemy_connection, replace=True, pg2=pg2_connection)
di.export_to_sql(google_reviews, 'google_reviews', con=sqlalchemy_connection, replace=True, pg2=pg2_connection)