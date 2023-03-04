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
    
    
    
