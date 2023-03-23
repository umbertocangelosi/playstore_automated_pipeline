import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.DataCleaner import DataCleaner
from src.DataIngestor import DataIngestor
di = DataIngestor()
dc = DataCleaner()
df = pd.read_csv(r'C:\Users\riccardo\Desktop\corso_programmazione\develhope_2023_team1\progetto_2\database\googleplaystore.csv')
dc.clean_all(df)

#1-split dataset into 4 parts and pickle them (search for pickle if you don't know what it is)
df_split = np.array_split(df, 4)
for i in range(4):
    df_split[i].to_pickle(R"./rick_pickle/split{i}.pkl")  

#2-unlock the pickling and merge the dataset as follow 2-4-1-3 


#3-reverse the whole data set (the last row will be the first one) 


#4-apply sliding window technic and store the patches in a 2D list


