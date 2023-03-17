import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from src.DataIngestor import DataIngestor
from src.DataCleaner import DataCleaner

di = DataIngestor()
df=di.read_csv("googleplaystore")
df=df.drop(10472)
dc=DataCleaner()
dc.cleanAll(df)
print(df[["App","Installs","Size","Reviews","Last Updated"]])

