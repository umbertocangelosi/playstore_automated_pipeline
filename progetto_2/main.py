import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from src.DataIngestor import DataIngestor
from src.DataCleaner import DataCleaner

dc = DataCleaner()
di = DataIngestor()

google_data = di.read_file(r"C:\Users\Alessio\Desktop\Progetti Team 1\develhope_2023_team1\progetto_2\database\googleplaystore.csv")

dc.clean_all(google_data)
print(google_data.info())