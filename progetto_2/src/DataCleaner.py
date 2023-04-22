import pandas as pd
import itertools

class DataCleaner:

    def __init__(self):
        pass
    
    
    def clean_google(self, dataframe):
        """
        Cleans main Google Play Store database.

        Args:
        - dataframe (pandas DataFrame): The raw database to be cleaned.

        Returns:
        - dataframe (pandas DataFrame): The cleaned database.
        """
        print("Cleaning main database")
        dataframe.drop(columns=['Current Ver', 'Android Ver', 'Last Updated'], inplace=True)
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
        """
        Cleans a dataframe containing Google Play Store reviews. It drops columns that are not necessary,
        removes rows with missing data, converts column names to lower case, filters the dataframe to include only
        reviews for apps that are in review dataframe, and returns the cleaned dataframe.
    
        Args:
        - dataframe (pandas DataFrame): The dataframe containing the Google Play Store reviews to be cleaned.
        - dataframe2 (pandas DataFrame): The dataframe containing the list of apps to include in the cleaned dataframe.
        
        Returns:
        - dataframe (pandas DataFrame): The cleaned dataframe.
        """
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
        """
        Take two lists containing positive and negative words respectively, flattens them, and combines
        them into a single list.

        Args:
        - lista_p (list): A list of positive words.
        - lista_n (list): A list of negative words.

        Returns:
        - list: A list containing all the words from both the positive and negative lists.
        """
        print("Cleaning good and bad database")
        negative = lista_n.values.tolist()
        positive = lista_p.values.tolist()        
        lista_appiattita_p = list(itertools.chain.from_iterable(positive))
        lista_appiattita_n = list(itertools.chain.from_iterable(negative))
        lista = lista_appiattita_n + lista_appiattita_p
        return lista


    def replace_common_strings(self, dataframe, col_name, string_list):
        """
        Replaces the value of the specified column of the given dataframe with matching words between the column and the given list.

        Args:
        - dataframe: a dataframe containing the column to be modified
        - col_name: the name of the column to be modified
        - string_list: a list of strings to be replaced in the column

        Returns:
        - dataframe: the modified dataframe
        """
        dataframe[col_name] = dataframe[col_name].apply(lambda x: " ".join([string for string in str(x).split() if string in string_list]))
        return dataframe
    

    def column_to_number(self,dataframe,column):
        """
        Converts the values in the specified column of the given dataframe to numeric 
        format by replacing unit abbreviations with their corresponding number of zeros.

        Args:
        - dataframe: a dataframe containing the column to be converted
        - column: the name of the column to be converted

        Returns:
        - dataframe: the modified dataframe with the specified column in numeric format
        """
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
        """
        Removes duplicate values from the specified column of the given dataframe.

        Args:
        - dataframe: a dataframe containing the column to be de-duplicated
        - column: the name of the column to be de-duplicated

        Returns:
        - dataframe: the modified dataframe with the specified column de-duplicated
        """
        dataframe=dataframe.drop_duplicates(subset=column, inplace=True)
        return dataframe
    
    
    def remove_na(self,dataframe,column):
        """
        Removes rows with missing data from the specified column of the given dataframe.

        Args:
        - dataframe: a dataframe containing the column to be cleaned
        - column: the name of the column to be cleaned

        Returns:
        - dataframe: the modified dataframe with the specified column cleaned of missing data
        """
        dataframe.dropna(subset=column,inplace=True)
        return dataframe


    def fill_na_median(self,dataframe,column):
        """
        Fills missing values in the specified column of the given dataframe with the median value of the column.

        Args:
        - dataframe: a dataframe containing the column to be cleaned
        - column: the name of the column to be cleaned

        Returns:
        - dataframe: the modified dataframe with the specified column cleaned of missing data
        """  
        dataframe[column].fillna(value=dataframe[column].median(),inplace=True)
        return dataframe


    def lower_case(self, dataframe):
        """
        Converts all column names and string values in the given dataframe to lowercase.

        Args:
        - dataframe: a dataframe to be converted to lowercase

        Returns:
        - dataframe: the modified dataframe with all column names and string values in lowercase
        """
        dataframe.columns = dataframe.columns.str.lower()
        dataframe.columns = ['_'.join(x.split()).lower() for x in dataframe.columns]
        for col in dataframe:
            dataframe[col] = dataframe[col].apply(lambda x: x.lower() if type(x) == str else x)
        return dataframe