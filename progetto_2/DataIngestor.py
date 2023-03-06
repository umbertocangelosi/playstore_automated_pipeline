import pandas as pd

class DataIngestor():
    def __init__(self) -> None:
        pass

    def create_csv(self, name_of_db,df):
        #metodo per creare un csv se non esistente dato come base il nome da assegnare al file csv e un database
        df.to_csv(f"./{name_of_db}.csv")
        pass

    def read_csv(self,name_of_csv):
        #metodo per leggere un file csv dato il nome del file csv
        df = pd.read_csv(f"{name_of_csv}.csv")
        return df
    
    def read_json(self,name_of_json):
        pass

    def read_html(self,url):
        pass
    
    # import/export generalizzato(richiamando funzioni senza self all'interno di una macrofunzione con self o singole funzioni per ogni tipo di operazione e formato?
    
    def transaction(self, operation='save',extension='txt',name='untitled'):
            
        if operation == 'save':
            if extension == 'csv':
                pass
            elif extension == 'txt':
                pass
            elif extension == 'json':
                pass
            pass
        
        elif operation == 'load':
            if extension == 'csv':
                pass
            elif extension == 'txt':
                pass
            elif extension == 'json':
                pass
            pass
        pass
    
    
    
