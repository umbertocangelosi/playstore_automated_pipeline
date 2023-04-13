import pandas as pd
import psycopg2
from sqlalchemy import create_engine

class DataIngestor():
    
    def __init__(self):
        pass

    def read_file (self, filepath):
        ext = filepath.split('.')[-1]
        if ext == 'csv':
            return pd.read_csv(filepath)
        elif ext == 'json':
            return pd.read_json(filepath)
        elif ext == 'htm' :
            return pd.read_html(filepath)
        elif ext == 'html' :
            return pd.read_html(filepath)
        elif ext =='xlsx':
            return pd.read_excel(filepath)
        elif ext == 'pkl':
            return pd.read_pickle(filepath)  
        else:
            return '\nfunction not implemented for this type of file yet\n'
    
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
    
    def sqlalchemy_connect(self,name,user,host,port):
        my_pass = input (f'\nInsert {name} password for {user} user: ')
        try:
            engine = create_engine(f'postgresql://{user}:{my_pass}@{host}:{port}/{name}') 
            print("\nConnection sqlalchemy\n")
            return engine
        except:
            print("\nError somewhere\n")  
    
    def to_cloud(self, dataframe, name, con, if_exists='fail', index=False):
        dataframe.to_sql(name=name, con=con, if_exists=if_exists, index=index)
        print(f"\n{dataframe} has been successfully uploaded!\n")

    def from_cloud(self, table):

        url = 'postgresql://onyhtqzn:ej-TLeomNZACBDKE7_PhUfZmCSUcFRW1@surus.db.elephantsql.com/onyhtqzn'
        alchemy_engine = create_engine(url=url)
        connection = alchemy_engine.connect()
        table = pd.read_sql(f'select * from "{table}"', connection)
        print(f'{table} has been loaded from our database online')
        return table