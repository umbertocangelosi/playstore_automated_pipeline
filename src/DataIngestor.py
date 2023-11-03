import pandas as pd
from sqlalchemy import create_engine

class DataIngestor():
    
    def __init__(self):
        self.url = 'postgresql://aljfqalc:eCoshU-kD2hhOB0mJg014ID64-m2e6Er@flora.db.elephantsql.com/aljfqalc'


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

    def to_cloud(self, dataframe, to_table, if_exists='replace', index=False):
        # dataframe : what we are pushing
        # to_table : table we are pushing to
        engine = create_engine(url=self.url)
        con = engine.connect()
        dataframe.to_sql(name=to_table, con=con, if_exists=if_exists, index=index)
        print(f"\n{dataframe} has been successfully uploaded!\n")

    def from_cloud(self, table):

        engine = create_engine(url=self.url)
        con = engine.connect()
        table = pd.read_sql(f'select * from "{table}"', con)
        print(f'{table} has been loaded from our database online')
        return table
