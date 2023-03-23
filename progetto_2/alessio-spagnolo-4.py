import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.DataCleaner import DataCleaner
from src.DataIngestor import DataIngestor
di = DataIngestor()
dc = DataCleaner()
google_dataframe = pd.read_csv(r'C:\Users\Alessio\Desktop\Progetti Team 1\develhope_2023_team1\progetto_2\database\googleplaystore.csv'
                               )
dc.clean_all(google_dataframe)

# # 5. Print a table and a plot chart for top 5 download apps with smallest size and highest downloading number

# top_smallest_downloaded = google_dataframe.sort_values(by=['Size','Installs'],ascending=[True,False]).head(5)
# print(top_smallest_downloaded)
# top_smallest_downloaded.plot.bar(x='App',y='Installs', color='Blue')
# plt.show()


# # 6. Print a table and a plot chart for top 5 download apps in each category free and paid (if there is paid)

# top_paid_apps = google_dataframe[google_dataframe['Type'] == 'Paid'].sort_values(by=['Installs','Rating','Price'],ascending=False).head(5)
# top_paid_apps['Installs'] = top_paid_apps['Installs'] / 2000000
# top_free_apps = google_dataframe[google_dataframe['Type'] == 'Free'].sort_values(by=['Installs','Rating','Reviews'],ascending=False).head(5)
# top_free_apps['Installs'] = top_free_apps['Installs'] / 200000000

# print(top_free_apps)
# print(top_paid_apps)

# top_free_apps.plot.bar(x='App',y=['Installs','Rating'])
# plt.show()
# top_paid_apps.plot.bar(x='App',y=['Installs','Rating'])
# plt.show()