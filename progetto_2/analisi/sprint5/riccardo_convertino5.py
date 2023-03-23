import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.DataCleaner import DataCleaner
from src.DataIngestor import DataIngestor
di = DataIngestor()
dc = DataCleaner()
df = pd.read_csv(r'C:\Users\riccardo\Desktop\corso_programmazione\develhope_2023_team1\progetto_2\database\googleplaystore.csv')
dc.clean_all(df)

print(df.isna().sum())