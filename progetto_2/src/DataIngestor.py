import pandas as pd
from sqlalchemy import create_engine

class DataIngestor():
    
    def __init__(self):
        self.url = 'postgresql://onyhtqzn:ej-TLeomNZACBDKE7_PhUfZmCSUcFRW1@surus.db.elephantsql.com/onyhtqzn'


    def read_file (self, filepath):
        """
        Reads a file from the specified filepath and returns a Pandas DataFrame.

        Args:
        - filepath: the filepath where the file to be read is located

        Returns:
        - a Pandas DataFrame containing the data from the specified file, or a message indicating that the function
        has not been implemented for the given file type
        """
        ext = filepath.split('.')[-1]
        if ext == 'csv':
            return pd.read_csv(filepath)
        elif ext == 'json':
            return pd.read_json(filepath)
        elif ext =='xlsx':
            return pd.read_excel(filepath)
        elif ext == 'pkl':
            return pd.read_pickle(filepath)  
        else:
            return '\nfunction not implemented for this type of file yet\n'

    def save_file (self, data, filepath):
        """
        Saves the given data to a file in the specified filepath in a format depending on the file extension.

        Args:
        - data: the data to be saved
        - filepath: the filepath where the data will be saved

        Returns:
        - None
        """ 
        ext = filepath.split('.')[-1]
        if ext == 'csv':
            return data.to_csv(filepath, index=False)
        elif ext == 'pkl':
            return data.to_pickle(filepath)
