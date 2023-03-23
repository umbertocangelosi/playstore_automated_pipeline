import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.DataCleaner import DataCleaner
from src.DataIngestor import DataIngestor
di = DataIngestor()
dc = DataCleaner()
google_dataframe = di.read_file(r'C:\Users\Alessio\Desktop\Progetti Team 1\develhope_2023_team1\progetto_2\database\googleplaystore.csv')
dc.clean_all(google_dataframe)

# 1 split dataset into 4 parts and pickle them

def create_chunks(dataframe):
    split_dataframe = np.array_split(dataframe, 4)
    i = 1
    for chunk in split_dataframe:
        pd.to_pickle(chunk,f'ale-split-part-{i}.pkl')
        i += 1

create_chunks(google_dataframe)

# 2 unlock the pickling and merge the dataset as follow 2-4-1-3 

chunk1 = pd.read_pickle(r"C:\Users\Alessio\Desktop\Progetti Team 1\develhope_2023_team1\progetto_2\ale-split-part-1.pkl")
chunk2 = pd.read_pickle(r"C:\Users\Alessio\Desktop\Progetti Team 1\develhope_2023_team1\progetto_2\ale-split-part-2.pkl")
chunk3 = pd.read_pickle(r"C:\Users\Alessio\Desktop\Progetti Team 1\develhope_2023_team1\progetto_2\ale-split-part-3.pkl")
chunk4 = pd.read_pickle(r"C:\Users\Alessio\Desktop\Progetti Team 1\develhope_2023_team1\progetto_2\ale-split-part-4.pkl")

merged_chunks = pd.concat([chunk2,chunk4,chunk1,chunk3], ignore_index=True)
print(merged_chunks)

# 3 reverse the whole data set (the last row will be the first one) 

reverse_google = google_dataframe.iloc[::-1,:]

# 4 apply sliding window technic and store the patches in a 2D list