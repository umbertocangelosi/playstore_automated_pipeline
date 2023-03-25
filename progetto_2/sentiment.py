import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from afinn import Afinn
from src.DataIngestor import DataIngestor
from src.DataCleaner import DataCleaner

# import and clean google dataset
afn = Afinn()
di = DataIngestor()
google_dataframe = di.read_file('./progetto_2/database/googleplaystore.csv')
dc = DataCleaner()
dc.clean_all(google_dataframe)

# import and clean google reviews dataset
reviews = di.read_file('./progetto_2/database/googleplaystore_user_reviews.csv')

# removing na values from review since it's important to know it's content, 26868 rows are filled with nan and we don't need them
dc.remove_na(reviews,'Translated_Review')

# removing unnecessary columns
reviews = reviews.drop(columns=['Sentiment', 'Sentiment_Polarity','Sentiment_Subjectivity'])

# UMBERTO?
reviews.reset_index(inplace=True)
reviews.drop('index',axis=1,inplace=True)
# end of cleaning

# creation of the list contains the negative and positive words to use with 'AFINN method'.
# UMBERTO?
negative = pd.read_excel('./progetto_2/database/n.xlsx')
negative = negative.values.tolist()
# UMBERTO?
positive = pd.read_excel('./progetto_2/database/p.xlsx')
positive = positive.values.tolist()

import itertools

# UMBERTO dicci tu cosa fa questo pezzo di codice
lista_appiattita_p = list(itertools.chain.from_iterable(positive))
lista_appiattita_n = list(itertools.chain.from_iterable(negative))
lista = lista_appiattita_n + lista_appiattita_p

# implement a function to fill ['Translated_Revies'] with matched words in the negative and positive words list and itself
def replace_common_strings(dataframe, col_name, string_list):
    dataframe[col_name] = dataframe[col_name].apply(lambda x: " ".join([string for string in str(x).split() if string in string_list]))
    return dataframe
# function call
replace_common_strings(reviews, 'Translated_Review', lista)

# creating Score column for each review
reviews['Score'] = reviews['Translated_Review'].apply(afn.score)

# grouping reviews dataframe by App name and calculating ['Score'] mean
app_score = reviews.groupby(by='App').agg({'Score':'mean'}).reset_index()

# merging ['Score'] mean to primary google dataset
google_dataframe = pd.merge(google_dataframe, app_score, how='left', on='App')

paid_apps = google_dataframe[google_dataframe['Type'] == 'Paid']

# 1 find if there is a correlation between the price of the apps and the category (Teen, Everyone, Mature). ➝ ANOVA: controlla se le medie in gruppi diversi sono significativamente differenti
price_by_content = google_dataframe.groupby(by='Content Rating')['Price'].mean()
price_by_content_only_paid = paid_apps.groupby(by='Content Rating')['Price'].mean()
price_by_content.plot.bar()
plt.title('All apps')
plt.xlabel('Category')
plt.ylabel('Average price')
plt.xticks(rotation = 13)
plt.show()
price_by_content_only_paid.plot.bar()
plt.title('Paid Apps')
plt.xlabel('Category')
plt.ylabel('Average price')
plt.xticks(rotation = 12)
plt.show()

# 2 find the sentiment of all apps using np files (negative words and positive words) and "afinn" lib 


# 3 for paid apps only list the top 5 highest and lowest sentiment numbers with the name of the app and the app category 

top_5_paid = paid_apps[["App","Category","Score"]].sort_values(by='Score',ascending=False).head(5)
worst_5_paid = paid_apps[["App","Category","Score"]].sort_values(by='Score',ascending=True).head(5)
print('\nThese are the best 5 paid apps according to our sentiment analysis\n')
print(top_5_paid)
print('\nThese are the worst 5 paid apps according to our sentiment analysis\n')
print(worst_5_paid)

# 4 what is the best category according to sentiment values
best_category = google_dataframe.groupby(by='Category')['Score'].mean().sort_values(ascending=False).head(1).index[0]
print(f'\nThe best category according to our sentiment analysis is: {best_category}\n')