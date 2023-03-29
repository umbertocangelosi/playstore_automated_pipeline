import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.DataCleaner import DataCleaner
from src.DataIngestor import DataIngestor
di = DataIngestor()
dc = DataCleaner()
google_dataframe = pd.read_csv(r'C:\Users\Alessio\Desktop\Progetti Team 1\develhope_2023_team1\progetto_2\database\googleplaystore.csv')
dc.clean_all(google_dataframe)

# 1. print unique names of all categories
print(google_dataframe['Category'].unique())

# 2. plot a bar chart for categories with the total number of installing numbers in each category 
google_categ = google_dataframe.groupby(by='Category')['Installs'].sum()
google_categ.plot.bar(color='DarkOrange')
plt.show()

# 3. plot a bar chart for the total prices of each paid app in each category ( the sum of all prices in the same category)
google_paid_categ = google_dataframe.groupby(by='Category')['Price'].sum()
google_paid_categ.plot.bar(color='DarkRed')
plt.show()

# 4. plot a bar chart of the total profit of each category by multiplying the price by the number of installs
google_paid_apps = google_dataframe[google_dataframe['Price']>0]
google_paid_apps['Profit'] = google_paid_apps['Price'] * google_paid_apps['Installs']
google_paid_apps_categ = google_paid_apps.groupby(by='Category')['Profit'].sum()
google_paid_apps_categ.plot.bar(color='DarkBlue')
plt.show()