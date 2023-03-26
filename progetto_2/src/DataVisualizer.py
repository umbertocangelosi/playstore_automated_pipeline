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
    def top_smallest(self, dataframe, column1='App', column2='Installs', library='sns', quantity=5):
        dataframe = dataframe.sort_values(by=['Size','Installs','Rating'], ascending=[True,False,False]).head(quantity)
        if library == 'plt':
            plt.bar(dataframe[column1], dataframe[column2])
        if library == 'sns':
            sns.barplot(data=dataframe, x=dataframe[column1], y=dataframe[column2])
        plt.xlabel('Apps')
        plt.ylabel('Downloads')
        plt.xticks(rotation=20)
        plt.show()

    # top 5 paid apps (based on installs->rating->review)

    def top_paid(self, dataframe, column1 = 'App', column2 = 'Installs', library = 'sns', quantity = 5):
        dataframe = dataframe[dataframe['Type'] == 'Paid'].sort_values(by=['Installs','Rating','reviews']).head(quantity)
        if library == 'plt':
            # top_paid_apps.plot.bar(x='App',y=['Installs','Rating'])            
            pass

        if library == 'sns':
            pass
    
    
    # plots based on business needs to take stock of the situation
    def visual_recap(self, dataframe):
        self.top_smallest(dataframe)
        self.top_paid(dataframe)



