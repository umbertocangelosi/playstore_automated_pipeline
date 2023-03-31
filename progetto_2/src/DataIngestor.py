import pandas as pd

class DataIngestor():
    def __init__(self) -> None:
        pass

    def read_file (self, filepath):
        ext = filepath[-4:]
        # metodo per leggere un file dato il nome del file e la sua estensione
        if ext == '.csv':
            return pd.read_csv(filepath)
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