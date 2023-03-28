import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.DataCleaner import DataCleaner
from src.DataIngestor import DataIngestor

di = DataIngestor()
dc = DataCleaner()
dataframe = di.read_file(.\progetto_2\database\googleplaystore.csv')
dc.clean_all(google_dataframe)

# 1

def create_chunks(dataframe):
    split_dataframe = np.array_split(dataframe, 4)
    i=0
    for chunk in split_dataframe:
        pd.to_pickle(chunk,f'chunk-{}.pkl')
        i=i+1

create_chunks(google_dataframe)

# 2  

chunk1 = pd.read_pickle(".\progetto2\chunk-1.pkl")
chunk2 = pd.read_pickle(".\progetto2\chunk-2.pkl")
chunk3 = pd.read_pickle(".\progetto2\chunk-3.pkl")
chunk4 = pd.read_pickle(".\progetto_2\chunk-4.pkl")

merged_chunks = pd.concat([chunk1,chunk2,chunk3,chunk4], ignore_index=True)
print(merged_chunks)

# 3 

reverse_google = google_dataframe.iloc[::-1,:]

