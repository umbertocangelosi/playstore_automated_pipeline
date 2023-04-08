import pandas as pd
import psycopg2
from sqlalchemy import create_engine

class DataIngestor():
    
    def __init__(self):
        pass

    def read_file (self, filepath):
        ext = filepath[-4:]
        name = filepath.split('\\')[-1]
        # metodo per leggere un file dato il nome del file e la sua estensione
        if ext == '.csv':
            file = pd.read_csv(filepath)
            file.name = name
            return file

        elif ext == 'json':
            return pd.read_json(filepath)
        elif ext == '.htm' :
            return pd.read_html(filepath)
        elif ext == 'html' :
            return pd.read_html(filepath)
        elif ext =='xlsx':
            return pd.read_excel(filepath)
        elif ext == '.pkl':
            return pd.read_pickle(filepath)  
        # will be implemented with future type of files needed
        else:
            return 'function not implemented for this type of file yet'
    
    def save_file (self, data, filepath):
        ext = filepath[-4:]
        # metodo per salvare un file
        if ext == '.csv':
            return data.to_csv(filepath, index=False)
        elif ext == 'json':
            return data.to_json(filepath, index=False)
        elif ext == '.htm' :
            return data.to_html(filepath, index=False)
        elif ext == 'html' :
            return data.to_html(filepath, index=False)
        elif ext == '.pkl':
            return data.to_pickle(filepath)
    '''la funzione crea un collegamento diretto con il database postgresql tramite la libreria psycopg2
    passandogli tutti i parametri, sicuramente sara conveniente assegnare il risultato a una variabile conn=di.connect()'''
    
    def connect(self,dbname,dbuser,dbpass,dbhost,dbport):
        DB_NAME = dbname
        DB_USER = dbuser
        DB_PASS = dbpass
        DB_HOST = dbhost
        DB_PORT = dbport

        try:
            conn = psycopg2.connect(database=DB_NAME,
                                    user=DB_USER,
                                    password=DB_PASS,
                                    host=DB_HOST,
                                    port=DB_PORT)
            print("Database connected successfully")
            print('Cursor object created')
            return conn
        except:
            print("Database not connected successfully")  
    

    
    #la funzione crea il database vuoto su postgres sfruttando il metodo .cursor() della classe conn, ossia la classe delle connessioni 
    #in psycopg2, tramite il metodo possiamo poi eseguire con execute() una query ddl per creare il database, ho assegnato come chiave primaria
    #il nome delle App. e' necessario fare commit dei cambiamenti effettuati nel rispetivo cursore.
    
    def create_google(self,conn):
        cur =conn.cursor()
        # executing queries to create table
        cur.execute("""
        DROP TABLE IF EXISTS googleplaystore CASCADE;

            CREATE TABLE IF NOT EXISTS googleplaystore
        (
            App TEXT PRIMARY KEY NOT NULL,
            Category TEXT NOT NULL,
            Rating INTEGER NOT NULL,
            Reviews INTEGER NOT NULL,
            Size INTEGER NOT NULL,
            Installs INTEGER NOT NULL,
            Type TEXT NOT NULL,
            Price FLOAT NOT NULL,
            Content_Rating TEXT NOT NULL,
            Genres TEXT NOT NULL,
            Last_Update TEXT NOT NULL
        )
                    """)
            #commit the changes
        conn.commit()
        print("Table Created successfully")
    
    '''qui ho creato una colonna con l'id seriale della recenzione, e ho creato il collegamento tra app di reviews e app di google'''
    def create_reviews(self,conn):
        cur =conn.cursor()

        # executing queries to create table
        cur.execute("""
        DROP TABLE IF EXISTS google_reviews CASCADE;

            CREATE TABLE IF NOT EXISTS google_reviews
        (   
            id SERIAL PRIMARY KEY,
            APP TEXT NOT NULL REFERENCES googleplaystore(APP),
            TRANSLATED_REVIEW TEXT NOT NULL 


        )
                    """)

        #commit the changes
        conn.commit()
        print("Table Created successfully")


    #qui sono obbligato a creare un'altra connessione come quella di psycopg2, ma usando sqlalchemy, perche' il metodo pd.to_sql() e' compatibile
    #con sqlalchemy e non con psycopg2
    def create_engine(self,username,password,host,port,database):
        try:
            engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}') 
            print("Created engine successfully")
            
            return engine
        
        except:
            print("Create engine failure")  
           

    #funzione che  carica il dataframe nella sua tabella, entrambi parametri da passare e che obbligatoriamente devono essere compatibili,
    #sono stato costretto a mettere quel parametro replace, perche' quando si caricano dei nuovi dati si deve poter scegliere di eliminare i dati precedenti
    #e inserire i nuovi, si potrebbe fare anche scrivendo replace al posto di 'append', ma dato che abbiamo un collegamento tra reviews e google in app,
    #non permette di rimpiazzare i dati e da errore tramite quel parametro
    def load(self,dataframe,tabella,engine,replace=False,conn=None):  

        if replace==True:
            cur=conn.cursor()
            cur.execute("""
        DROP TABLE IF EXISTS tabella CASCADE;
        """)

        
        dataframe.to_sql(tabella, con=engine, if_exists='append', index=False)
        print('Load to postgres success')
       