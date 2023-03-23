import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.DataCleaner import DataCleaner
from src.DataIngestor import DataIngestor
di = DataIngestor()
dc = DataCleaner()
df = pd.read_csv(r'.\progetto_2\database\googleplaystore.csv')
dc.clean_all(df)


#1-split dataset into 4 parts and pickle them (search for pickle if you don't know what it is)

df_split = np.array_split(df, 4)
 
# for i in range(4):
#         df_split.to_pickle(f"./split{i}.pkl")
pickle0=pd.read_pickle("./split0.pkl")
pickle1=pd.read_pickle("./split1.pkl")
pickle2=pd.read_pickle("./split2.pkl")
pickle3=pd.read_pickle("./split3.pkl")

#2-unlock the pickling and merge the dataset as follow 2-4-1-3 ## 1-3-0-2
df_merged=pd.concat([pickle1,pickle3,pickle0,pickle2], ignore_index=True)
#print(df_merged)

#3-reverse the whole data set (the last row will be the first one) 
df_reverse = df.iloc[::-1]
print(df_reverse)

#4-apply sliding window technic and store the patches in a 2D list
    

