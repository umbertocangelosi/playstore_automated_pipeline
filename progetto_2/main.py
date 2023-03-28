import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from src.DataIngestor import DataIngestor
di = DataIngestor()
from src.DataCleaner import DataCleaner
dc = DataCleaner()
from src.DataVisualizer import DataVisualizer
dv = DataVisualizer()

google_data = di.read_file("./progetto_2/database/googleplaystore.csv")
dc.clean_all(google_data)
di.save_file(google_data, "./progetto_2/database/googleplaystore_cleaned.csv")