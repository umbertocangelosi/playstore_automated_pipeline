import pandas as pd
import psycopg2
from sqlalchemy import create_engine

class DataIngestor():
    
    def __init__(self):
        pass

    def read_file (self, filepath):
        # name = filepath.split('.')[-2].split('/')[-1]
        ext = filepath.split('.')[-1]
        if ext == 'csv':
            file = pd.read_csv(filepath)
            return file
        elif ext == 'json':
            file = pd.read_json(filepath)
            return file
        elif ext == 'htm' :
            file = pd.read_html(filepath)
            return file
        elif ext == 'html' :
            file = pd.read_html(filepath)
            return file
        elif ext =='xlsx':
            file = pd.read_excel(filepath)
            return file
        elif ext == 'pkl':
            file = pd.read_pickle(filepath)  
            return file
        else:
            return 'function not implemented for this type of file yet'
    
    def save_file (self, data, filepath):
        ext = filepath.split('.')[-1]
        if ext == 'csv':
            return data.to_csv(filepath, index=False)
        elif ext == 'json':
            return data.to_json(filepath, index=False)
        elif ext == 'htm' :
            return data.to_html(filepath, index=False)
        elif ext == 'html' :
            return data.to_html(filepath, index=False)
        elif ext == 'pkl':
            return data.to_pickle(filepath)
        
    '''la funzione crea un collegamento diretto con il database postgresql tramite la libreria psycopg2
    passandogli tutti i parametri, sicuramente sara conveniente assegnare il risultato a una variabile conn=di.connect()'''
    
    def connect(self,dbname,dbuser,dbhost,dbport):
        dbpass = input (f'Insert {dbname} password for {dbuser} user: ')
        try:
            conn = psycopg2.connect(database=dbname,
                                    user=dbuser,
                                    password=dbpass,
                                    host=dbhost,
                                    port=dbport)
            print("Database connected successfully")
            print('Cursor object created')
            return conn
        except:
            print("Database not connected successfully")  
    

    
    #la funzione crea il database vuoto su postgres sfruttando il metodo .cursor() della classe conn, ossia la classe delle connessioni 
    #in psycopg2, tramite il metodo possiamo poi eseguire con execute() una query ddl per creare il database, ho assegnato come chiave primaria
    #il nome delle App. e' necessario fare commit dei cambiamenti effettuati nel rispetivo cursore.
    
    def create_google(self,conn):
        cur = conn.cursor()
        # executing queries to create table
        cur.execute("""
        DROP TABLE IF EXISTS googleplaystore CASCADE;

            CREATE TABLE IF NOT EXISTS googleplaystore
        (
            app TEXT PRIMARY KEY NOT NULL,
            category TEXT NOT NULL,
            rating INTEGER NOT NULL, qua per esempio rating non dovrebbe essere un float?
            reviews INTEGER NOT NULL,
            size INTEGER NOT NULL,
            installs INTEGER NOT NULL,
            type TEXT NOT NULL,
            price FLOAT NOT NULL,
            content_Rating TEXT NOT NULL,
            genres TEXT NOT NULL,
            last_Update TEXT NOT NULL
        )
                    """)
            #commit the changes
        conn.commit()
        print("Table Created successfully")
    
    '''qui ho creato una colonna con l'id seriale della recensione, e ho creato il collegamento tra app di reviews e app di google'''
    def create_reviews(self,conn):
        cur = conn.cursor()

        # executing queries to create table
        cur.execute("""
        DROP TABLE IF EXISTS google_reviews CASCADE;

            CREATE TABLE IF NOT EXISTS google_reviews
        (   
            id SERIAL PRIMARY KEY,
            app TEXT NOT NULL REFERENCES googleplaystore(APP),
            translated_review TEXT NOT NULL 


        )
                    """)

        #commit the changes
        conn.commit()
        print("Table Created successfully")

# dbname,dbuser,dbhost,dbport
    #qui sono obbligato a creare un'altra connessione come quella di psycopg2, ma usando sqlalchemy, perche' il metodo pd.to_sql() e' compatibile
    #con sqlalchemy e non con psycopg2
    def create_engine(self,dbname,dbuser,dbhost,dbport,dbpass):
        dbpass = input (f'Insert {dbname} password for {dbuser} user: ')
        try:
            engine = create_engine(f'postgresql://{dbuser}:{dbpass}@{dbhost}:{dbport}/{dbname}') 
            print("Engine created successfully")
            return engine
        except:
            print("Error somewhere")  
           

    #funzione che  carica il dataframe nella sua tabella, entrambi parametri da passare e che obbligatoriamente devono essere compatibili,
    #sono stato costretto a mettere quel parametro replace, perche' quando si caricano dei nuovi dati si deve poter scegliere di eliminare i dati precedenti
    #e inserire i nuovi, si potrebbe fare anche scrivendo replace al posto di 'append', ma dato che abbiamo un collegamento tra reviews e google in app,
    #non permette di rimpiazzare i dati e da errore tramite quel parametro
    def load(self, dataframe, table, engine, replace=False, conn=None):  

        if replace:
            cur = conn.cursor()
            cur.execute("""
        DROP TABLE IF EXISTS tabella CASCADE;
        """)

        
        dataframe.to_sql(table, con=engine, if_exists='append', index=False)
        print('Load to postgres success')
       