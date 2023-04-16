import pandas as pd
#import psycopg2
import enum
import numpy as np
import psycopg2
from sqlalchemy import create_engine  
from sqlalchemy import Table, Column, String, MetaData
import sqlalchemy as db


class DbHandler():
    
    def __init__(self):
        pass

       
    '''la funzione crea un collegamento diretto con il database postgresql tramite la libreria psycopg2
    passandogli tutti i parametri, sicuramente sara conveniente assegnare il risultato a una variabile conn=di.connect()'''
    
    def pg2_connect(self,dbname,dbuser,dbhost,dbport):

        dbpass = "ej-TLeomNZACBDKE7_PhUfZmCSUcFRW1"

        try:
            conn = psycopg2.connect(database=dbname,
                                    user=dbuser,
                                    password=dbpass,
                                    host=dbhost,
                                    port=dbport)
            print("\nConnection established")
            print("\nCursor object created")
            return conn
        
        except:
            print("\nConnection failed\n")  
    

    
    #la funzione crea il database vuoto su postgres sfruttando il metodo .cursor() della classe conn, ossia la classe delle connessioni 
    #in psycopg2, tramite il metodo possiamo poi eseguire con execute() una query ddl per creare il database, ho assegnato come chiave primaria
    #il nome delle App. e' necessario fare commit dei cambiamenti effettuati nel rispettivo cursore.
    
    def create_table_google(self, engine):

        connection = engine.connect()
        metadata = db.MetaData()

        google_play_store = db.Table(
            'google_play_store', 
            metadata,
            db.Column('app', db.String(255), primary_key=True, nullable=False),
            db.Column('category', db.String(255), nullable=False),
            db.Column('rating', db.Float(), nullable=False),
            db.Column('reviews', db.Integer(), nullable=False),
            db.Column('size', db.Integer(), nullable=False),
            db.Column('installs', db.Integer(), nullable=False),
            db.Column('type', db.String(255), nullable=False),
            db.Column('price', db.Float(), nullable=False),
            db.Column('content_rating', db.String(255), nullable=False),
            db.Column('genres', db.String(255), nullable=False),
            db.Column('last_updated', db.String(255), nullable=False),
        )

        metadata.create_all(engine)
        print("Table google_play_store created!")
        
    

    def create_table_reviews(self,engine):

        connection = engine.connect()
        metadata2 = db.MetaData()
        
        google_reviews = db.Table(
            'google_reviews', 
            metadata2,
            db.Column('id', db.Integer(), autoincrement=True, primary_key=True),
            db.Column('app', db.String(255), db.ForeignKey("google_play_store.app"), nullable=False),
            db.Column('translated_review', db.String(255), nullable=False),
        )


        metadata2.create_all(engine) 
        
        print("Table google_reviews created!")

# dbname,dbuser,dbhost,dbport
# qui sono obbligato a creare un'altra connessione come quella di psycopg2, ma usando sqlalchemy, perche' il metodo pd.to_sql() e' compatibile
# con sqlalchemy e non con psycopg2
    def sqlalchemy_connect(self):

        #my_pass = input (f'Insert {name} password for {user} user: ')

        try:
            #engine = create_engine(f'postgresql+psycopg2://{user}:{my_pass}@{host}:{port}/{name}') 
            engine = create_engine(f'postgresql://onyhtqzn:ej-TLeomNZACBDKE7_PhUfZmCSUcFRW1@surus.db.elephantsql.com/onyhtqzn')
            print("Connection sqlalchemy")
            return engine
        except:
            print("Error somewhere")  
           

#funzione che carica il dataframe nella sua tabella, entrambi parametri da passare e che obbligatoriamente devono essere compatibili,
#sono stato costretto a mettere quel parametro replace, perche' quando si caricano dei nuovi dati si deve poter scegliere di eliminare i dati precedenti
#e inserire i nuovi, si potrebbe fare anche scrivendo replace al posto di 'append', ma dato che abbiamo un collegamento tra reviews e google in app,
#non permette di rimpiazzare i dati e da errore tramite quel parametro
    
    def export_to_sql(self, dataframe, name, con, replace=False, pg2=None):

        if replace:
            cur = pg2.cursor()
            cur.execute("""
        DROP TABLE IF EXISTS dataframe CASCADE;
        """)

        
        dataframe.to_sql(name=name, con=con, if_exists='append', index=False)
        print("Load to postgres success")
