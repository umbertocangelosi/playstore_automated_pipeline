import pandas as pd
import itertools

class DataCleaner:

    def __init__(self):
        pass
    
    def clean_googledb(self, dataframe):

        print("Cleaning main database")
        dataframe.drop(columns=['Current Ver', 'Android Ver'], inplace=True)
        self.column_to_number(dataframe, 'Installs')
        self.column_to_number(dataframe, 'Size')
        self.column_to_number(dataframe, 'Reviews')
        self.column_to_number(dataframe, 'Price')
        self.lower_case(dataframe)
        self.remove_column_duplicates(dataframe, 'app')
        self.remove_na(dataframe, 'app')
        self.remove_na(dataframe, 'type')
        self.fill_na_median(dataframe, 'size')
        self.fill_na_median(dataframe, 'rating')
        return dataframe
    
    def clean_google_reviews(self, dataframe, dataframe2):
        print("Cleaning reviews database")
        dataframe.drop(columns=['Sentiment', 'Sentiment_Polarity', 'Sentiment_Subjectivity'], inplace=True)
        dataframe = dataframe.dropna()
        dataframe.reset_index(inplace=True)
        dataframe.drop('index', axis=1, inplace=True)
        self.lower_case(dataframe)
        dataframe['translated_review'] = dataframe['translated_review'].astype(str)
        dataframe = dataframe[dataframe['app'].isin(dataframe2['app'])]
        return dataframe
    
    def clean_sentiment_list(self, lista_p, lista_n):
        print("Cleaning good and bad database")
        negative = lista_n.values.tolist()
        positive = lista_p.values.tolist()        
        lista_appiattita_p = list(itertools.chain.from_iterable(positive))
        lista_appiattita_n = list(itertools.chain.from_iterable(negative))
        lista = lista_appiattita_n + lista_appiattita_p
        return lista

    def replace_common_strings(self, dataframe, col_name, string_list):
        dataframe[col_name] = dataframe[col_name].apply(lambda x: " ".join([string for string in str(x).split() if string in string_list]))
        return dataframe
    
    def column_to_number(self,dataframe,column):
        dataframe[column] = dataframe[column].astype(str).replace("Varies with device",'')
        # replacing Giga with 9 zeros
        dataframe[column] = dataframe[column].str.replace('G','000000000')
        # replacing Mega with 6 zeros
        dataframe[column] = dataframe[column].str.replace('M','000000')
        # replacing kilo with 3 zeros
        dataframe[column] = dataframe[column].str.replace('k','000')
        dataframe[column] = pd.to_numeric(dataframe[column].str.replace('[^0-9.]', '',regex=True))
        return dataframe

    def remove_column_duplicates(self,dataframe,column):
        dataframe=dataframe.drop_duplicates(subset=column, inplace=True)
        return dataframe
    
    # Handling missing data
    
    def remove_na(self,dataframe,column):
        #remove rows with missing revelant data
        dataframe.dropna(subset=column,inplace=True)
        return dataframe

    def fill_na_median(self,dataframe,column):

        # fill empty values with median
        dataframe[column].fillna(value=dataframe[column].median(),inplace=True)
        return dataframe
    
    # standardize text in lower case

    def lower_case(self, dataframe):

        dataframe.columns = dataframe.columns.str.lower()
        dataframe.columns = ['_'.join(x.split()).lower() for x in dataframe.columns]
        for col in dataframe:
            dataframe[col] = dataframe[col].apply(lambda x: x.lower() if type(x) == str else x)
        return dataframe
    
