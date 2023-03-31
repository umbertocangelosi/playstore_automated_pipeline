import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from DataCleaner import DataCleaner
from DataIngestor import DataIngestor
di = DataIngestor()
dc = DataCleaner()

df = pd.read_csv(r'C:\Users\riccardo\Desktop\corso_programmazione\Team1_Work\project2\analisi\sprint4/googleplaystore.csv').drop(10472)
dc.clean_all(df)

#Print a table and a plot chart for top 5 download apps with smallest size and highest downloading number

# df_small_down = df.sort_values(['Size','Installs']).head(5)
# print(df_small_down)
# df_small_down.plot.bar(x='App',y='Installs')
# plt.show()


#Print a table and a plot chart for top 5 download apps in each category free and paid (if there is paid)

df_5paid_apps = df[df['Type'] == 'Paid'].sort_values(['Installs','Rating','Price'],ascending=False).head(5)
df_5paid_apps['Reviews'] = df_5paid_apps['Reviews'] / 500000
df_5paid_apps['Installs'] = df_5paid_apps['Installs'] / 2000000


df_5free_apps = df[df['Type'] == 'Free'].sort_values(['Installs','Rating','Reviews'],ascending=False).head(5)
df_5free_apps['Reviews'] = df_5free_apps['Reviews'] / 15000000
df_5free_apps['Installs'] = df_5free_apps['Installs'] / 200000000


print(df_5paid_apps[['Installs','Rating','Reviews']])
print(df_5free_apps[['Installs','Rating','Reviews']])


df_5free_apps.plot.bar(x='App',y=['Installs','Rating','Reviews'])
plt.show()
df_5paid_apps.plot.bar(x='App',y=['Installs','Rating','Reviews'])
plt.show()