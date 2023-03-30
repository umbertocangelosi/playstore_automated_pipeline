import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from afinn import Afinn
afn = Afinn()


class DataVisualizer:
    def __init__(self):
        sns.set()

    # Top 5 Apps with smallest size and highest downloads
    # just select the dataframe
    # if app and installs columns were renamed, then use new names as parameters of column 1&2
    def top_smallest(self, dataframe, column1='App', column2='Installs', library='sns', quantity=5):
        dataframe = dataframe.sort_values(by=['Size','Installs','Rating'], ascending=[True,False,False]).head(quantity)
        if library == 'plt':
            plt.bar(dataframe[column1], dataframe[column2])
        if library == 'sns':
            sns.barplot(data=dataframe, x=dataframe[column1], y=dataframe[column2])
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.xticks(rotation=20)
        plt.show()

    # top 5 paid apps (based on installs->rating->review)

    def top_paid(self, dataframe, column1='App', column2='Installs', library='sns', quantity=5):
        dataframe = dataframe[dataframe['Type'] == 'Paid'].sort_values(by=['Installs','Rating','Reviews'],ascending=False).head(quantity)
        if library == 'plt':
            plt.bar(dataframe[column1], dataframe[column2])
        if library == 'sns':
            sns.barplot(data=dataframe, x=dataframe[column1], y=dataframe[column2])
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.xticks(rotation=20)
        plt.show()

    def scatter_corr(self, dataframe, column1, column2, library='sns'):
        if library == 'sns':
            sns.scatterplot(data=dataframe, x=column1, y=column2, hue='Content Rating', size='Type',legend='full')

        if library == 'plt':
            plt.scatter(dataframe[column1],dataframe[column2])
        
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.xticks(rotation=20)
        plt.show()


    # plots based on business needs to take stock of the situation
    def visual_recap(self, dataframe, quantity=5):
        pass
        #self.top_smallest(dataframe,quantity)
        #self.top_paid(dataframe,quantity)


    # top 5 higher installs / chiedere per aggiungere piu colonne all'asse y
    def top_apps(self, dataframe, column1='App', column2='Installs', library='sns', quantity=5):
        dataframe = dataframe.sort_values(by=['Installs','Rating','Reviews'],ascending=False).head(quantity)
        if library == 'plt':
            plt.bar(dataframe[column1], height=dataframe[column2])
        if library == 'sns':
            sns.barplot(data=dataframe, x=dataframe[column1], y=dataframe[column2]) # hue 
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.xticks(rotation=12)
        plt.show()

    # top categories by rating(mean)
    def top_categories(self, dataframe, library='sns'):
        plt.figure(figsize=(18,10))  
        series_cat = dataframe.groupby("Category")["Rating"].mean()
        series_cat_df=series_cat.reset_index()
        series_cat_df.columns= ['Category', 'Ratingmean']
        if library == 'plt':
            plt.bar(series_cat_df["Category"], series_cat_df["Ratingmean"])
        if library == 'sns':
            sns.barplot(data=series_cat_df, x="Category",y="Ratingmean")
        plt.xticks(rotation=12)
        plt.show()

      
    # top 5 paid categories by price(sum)
    def top_paid_categories(self, dataframe, library='sns',quantity=5):
        series_cat = dataframe.groupby("Category")["Price"].sum()
        series_cat_df=series_cat.reset_index().sort_values(by='Price',ascending=False).head(quantity)
        series_cat_df.columns= ['Category', 'PriceSum']
        if library == 'plt':
            plt.bar(series_cat_df["Category"], series_cat_df["PriceSum"])
        if library == 'sns':
            sns.barplot(data=series_cat_df, x="Category",y="PriceSum")
        plt.xticks(rotation=12)
        plt.show()

    # find if there is a correlation between the price of the apps and the category (Teen, Everyone, Mature).
    def avg_price_users(self, dataframe, library='sns'):
        paid_apps = dataframe[dataframe['Type'] == 'Paid']
        price_by_content_only_paid = paid_apps.groupby(by='Content Rating')['Price'].mean()
        price_by_content_only_paid_df=price_by_content_only_paid.reset_index()
        price_by_content_only_paid_df.columns= ['Content Rating', 'Pricemean']
        if library == 'plt':
            plt.bar(price_by_content_only_paid_df["Content Rating"], price_by_content_only_paid_df["Pricemean"])
        if library == 'sns':
            sns.barplot(data=price_by_content_only_paid_df, x="Content Rating",y="Pricemean")
        plt.title('Paid Apps')
        plt.xlabel('Category')
        plt.ylabel('Average price')
        plt.xticks(rotation = 4)
        plt.show()

    # top FREE apps by SENTIMENT
    def top_free_by_sentiment(self,dataframe, column1='App', column2='Score', library='sns', quantity=5):
        plt.figure(figsize=(16,6))  
        dataframe = dataframe[dataframe['Type'] == 'Free'][["App","Score"]].sort_values(by='Score',ascending=False).head(quantity)
        if library == 'plt':
            plt.bar(dataframe[column1], dataframe[column2])
        if library == 'sns':
            sns.barplot(data=dataframe, x=dataframe[column1], y=dataframe[column2])
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.xticks(rotation=5)
        plt.title(f'Top {quantity} free Apps by sentiment')
        plt.show()
    
    # worst FREE apps by SENTIMENT
    def worst_free_by_sentiment(self,dataframe, column2='App', column1='Score', library='sns', quantity=5):
        dataframe = dataframe[dataframe['Type'] == 'Free'][["App","Score"]].sort_values(by='Score',ascending=True).head(quantity)
        
        if library == 'plt':
            plt.bar(dataframe[column1], dataframe[column2])
        if library == 'sns':
            sns.barplot(data=dataframe, x=dataframe[column1], y=dataframe[column2])
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.title(f'Worst {quantity} Apps by sentiment score')
        plt.show()
    
    # worst PAID apps by SENTIMENT
    def worst_paid_by_sentiment(self,dataframe, column2='App', column1='Score', library='sns', quantity=5):
        dataframe = dataframe[dataframe['Type'] == 'Paid'][["App","Category","Score"]].sort_values(by='Score',ascending=True).head(quantity)
        if library == 'plt':
            plt.bar(dataframe[column1], dataframe[column2])
        if library == 'sns':
            sns.barplot(data=dataframe, x=dataframe[column1], y=dataframe[column2])
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.title(f'Worst {quantity} paid Apps by sentiment score')
        plt.show()        
    
    # top PAID apps by SENTIMENT
    def top_paid_by_sentiment(self,dataframe, column2='App', column1='Score', library='sns', quantity=5):
        dataframe = dataframe[dataframe['Type'] == 'Paid'][["App","Category","Score"]].sort_values(by='Score',ascending=False).head(quantity)
        if library == 'plt':
            plt.bar(dataframe[column1], dataframe[column2])
        if library == 'sns':
            sns.barplot(data=dataframe, x=dataframe[column1], y=dataframe[column2])
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.title('Top 5 paid Apps by sentiment score')
        plt.show()
        
    def global_by_sentiment(self,dataframe, column1='App', column2='Score', library='sns', quantity=5):
      
        dataframe.dropna(subset='Score',axis=0,inplace=True)
        dataframe = dataframe[["App","Score",'Type']].sort_values(by='Score',ascending=False)       
        dataframe_paid=dataframe[dataframe.Type=='Paid']
        dataframe_free=dataframe[dataframe.Type=='Free']
        dataframe_paid=pd.concat([dataframe_paid.head(quantity),dataframe_paid.tail(quantity)])
        dataframe_free=pd.concat([dataframe_free.head(quantity),dataframe_free.tail(quantity)])
       
        fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(18,10))

        if library == 'plt':
            ax1.bar(dataframe_paid[column1], dataframe_paid[column2])
            ax1.set_title("Top 5 and worst 5 paid Apps by sentiment score")
            ax2.bar(dataframe_free[column1],dataframe_free[column2])
            ax2.set_title("Top 5 and worst 5 free Apps by sentiment score")
        
        if library == 'sns':
            sns.barplot(data=dataframe_paid, x=dataframe_paid[column1], y=dataframe_paid[column2],ax=ax1)
            ax1.set_title("Top 5 and worst 5 paid Apps by sentiment score")
            sns.barplot(data=dataframe_free, x=dataframe_free[column1], y=dataframe_free[column2],ax=ax2)
            ax2.set_title("Top 5 and worst 5 free Apps by sentiment score")
        plt.xlabel(column1)
        plt.ylabel(column2)
        ax1.tick_params(axis='x',rotation=10)
        ax2.tick_params(axis='x',rotation=10)
        plt.show()        
   
    def categories_by_sentiment(self,dataframe, column2='Category', column1='Score', library='sns'):
       
        if library == 'plt':
            dataframe = dataframe.groupby(by='Category')['Score'].mean().sort_values(ascending=False)
            dataframe.index.name('Category')
            plt.barh(dataframe[column2])
            
        if library == 'sns':
            sns.barplot(data=dataframe, y="Category", x="Score")
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.title('Worst 5 Apps by sentiment score')
        plt.show()








