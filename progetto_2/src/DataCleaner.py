# print(df['Size'][df['Size'] != 'Varies with device'][~df['Size'].str.contains('M')[~df['Size'].str.contains('k')])
import pandas as pd
# def column_to_number2(df,col):
#     df[col] = df[col].str.replace("Varies with device",'')
#     df[col] = df[col].str.replace('M', '000000')
#     df[col] = df[col].str.replace('k','000')
#     df[col] = pd.to_numeric(df[col].str.replace('[^0-9.]', '',regex=True))
#     return df

class DataCleaner:
    
    def __init__(self,):
        pass
    
    def clean_all(self, dataframe):
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
            
    #     # leave only numbers and dots, then cast to int64
    #     return dataframe
    
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
        # replace commas with dots, working so far
        dataframe[column] = dataframe[column].str.replace(',','.')
        return dataframe

    def remove_dots(self,dataframe,column):
        # remove dots from a column
        dataframe[column] = dataframe[column].str.replace('.','')
        return dataframe

    # def size_to_number():
    #     # replace (M with '000',k with '',G with '000000'). output in mega
    #     pass
    
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
