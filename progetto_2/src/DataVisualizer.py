import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from afinn import Afinn
afn = Afinn()

class DataVisualizer:

    def __init__(self):
        pass

    # Top 5 Apps with smallest size and highest downloads
    # just select the dataframe
    # if app and installs columns were renamed, then use new names as parameters of column 1&2

    def top_small(self, dataframe, column1 = 'App', column2 = 'Installs', library = 'sns', quantity = 5):
        dataframe = dataframe.sort_values(by=['Size','Installs','Rating'], ascending=[True,False,False]).head(quantity)
        if library == 'plt':
            # top_smallest_downloaded.plot.bar(x='App',y='Installs', color='Blue')
            # plt.show()         
            pass

        if library == 'sns':
            pass

    # top 5 paid apps (based on installs->rating->review)

    def top_paid(self, dataframe, column1 = 'App', column2 = 'Installs', library = 'sns', quantity = 5):
        dataframe = dataframe[dataframe['Type'] == 'Paid'].sort_values(by=['Installs','Rating','Price'],ascending=False).head(quantity)
        if library == 'plt':
            # top_paid_apps.plot.bar(x='App',y=['Installs','Rating'])            
            pass

        if library == 'sns':
            pass



