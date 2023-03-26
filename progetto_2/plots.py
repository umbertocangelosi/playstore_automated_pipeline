import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from src.DataIngestor import DataIngestor
from src.DataCleaner import DataCleaner
from src.DataVisualizer import DataVisualizer

dc = DataCleaner()
di = DataIngestor()
dv = DataVisualizer()

google_data = di.read_file("./progetto_2/database/googleplaystore_cleaned.csv")

dv.top_5_small(google_data, library='plt')