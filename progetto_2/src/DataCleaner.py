import pandas as pd
import itertools

class DataCleaner:

    def __init__(self):
        pass
    
    def clean_googledb(self, dataframe):

        print("Cleaning main database")
        dataframe.drop(columns=['Current Ver', 'Android Ver'], inplace=True)
        self.column_to_number(dataframe, "Installs")
        self.column_to_number(dataframe, "Size")
        self.column_to_number(dataframe, "Reviews")
        self.column_to_number(dataframe, 'Price')
        self.remove_column_duplicates(dataframe,"App")
        self.remove_na(dataframe,"App")
        self.fill_na_median(dataframe, 'Size')
        self.fill_na_median(dataframe, 'Rating')
        #self.date_conversion(dataframe,"Last Updated")
        return dataframe
    
    def clean_googlereviews(self, dataframe):
        print("Cleaning reviews database")
        dataframe.drop(columns=['Sentiment', 'Sentiment_Polarity','Sentiment_Subjectivity'], inplace=True)
        self.remove_na(dataframe,'Translated_Review')
        dataframe.reset_index(inplace=True)
        dataframe.drop('index',axis=1,inplace=True)
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

    def comma_to_dot(self,dataframe,column):
        # replace commas with dots
        dataframe[column] = dataframe[column].str.replace(',','.')
        return dataframe

    def remove_dots(self,dataframe,column):
        # remove dots from a column
        dataframe[column] = dataframe[column].str.replace('.','')
        return dataframe
    
    def remove_column_duplicates(self,dataframe,column):
        # remove duplicates entries with the same Name, platform, genre
        dataframe=dataframe.drop_duplicates(subset=column, inplace=True)
        return dataframe

    def standardize_text(self,dataframe,column):
        # return all entries of a column in string lower case/title/capitalize, based on the parameter format
        if dataframe[column].dtype != int:
            dataframe[column] = dataframe[column].str.lower()
            return dataframe
        else:
            print('Column is filled with integers\nAborting function')
            pass
    
    def date_conversion(self,dataframe,column):
        dataframe[column] = pd.to_datetime(dataframe[column])
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

#     dataframe = dataframe.assign(**{column: pd.to_numeric(dataframe[column].str.replace('[^0-9.]', '', regex=True))})