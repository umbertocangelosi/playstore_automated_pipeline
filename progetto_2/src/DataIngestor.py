import pandas as pd

class DataIngestor():
    def __init__(self) -> None:
        pass

    def create_csv(self, file_name, dataframe):
        #metodo per creare un csv se non esistente dato come base il nome da assegnare al file csv e un database
        dataframe.to_csv(f"./{file_name}.csv")
        pass

    def read_file (self, filepath):
        ext = filepath[-3:]
        # metodo per leggere un file dato il nome del file e la sua estensione
        if ext == 'csv':
            return pd.read_csv(filepath)
        elif ext == 'json':
            return pd.read_json(filepath)
        elif ext == 'htm' :
            return pd.read_html(filepath)
        elif ext == 'html' :
            return pd.read_html(filepath)
        # will be implemented with future type of files needed
        else:
            print('function not implemented for this type of file yet')
            pass 