# print(df['Size'][df['Size'] != 'Varies with device'][~df['Size'].str.contains('M')[~df['Size'].str.contains('k')])
import pandas as pd
# def column_to_number2(df,col):
#     df[col] = df[col].str.replace("Varies with device",'')
#     df[col] = df[col].str.replace('M', '000000')
#     df[col] = df[col].str.replace('k','000')
#     df[col] = pd.to_numeric(df[col].str.replace('[^0-9.]', '',regex=True))
#     return df

class DataCleaner:
    
    def __init__(self):
        pass
    
    # def to_number(self,dataframe,column):
        
    #     # leave only numbers and dots, then cast to int64
    #     dataframe = dataframe.assign(**{column: pd.to_numeric(dataframe[column].str.replace('[^0-9.]', '', regex=True))})
    #     return dataframe
    
    def column_to_number(dataframe,column):
        dataframe[column] = dataframe[column].str.replace("Varies with device",'')
        # replacing Giga with 9 zeros
        dataframe[column] = dataframe[column].str.replace('G','000000000')
        # replacing Mega with 6 zeros
        dataframe[column] = dataframe[column].str.replace('M','000000')
        # replacing kilo with 3 zeros
        dataframe[column] = dataframe[column].str.replace('k','000')
        dataframe[column] = pd.to_numeric(dataframe[column].str.replace('[^0-9.]', '',regex=True))
        return dataframe

    def comma_to_dot(dataframe,column):
        # replace commas with dots, working so far
        dataframe[column] = dataframe[column].str.replace(',','.')
        return dataframe

    def remove_dots(dataframe,column):
        # remove dots from a column
        dataframe[column] = dataframe[column].str.replace('.','')
        return dataframe

    # def size_to_number():
    #     # replace (M with '000',k with '',G with '000000'). output in mega
    #     pass

    # def convert_date():
    #     # convert date from string to date
    #     pass
    
    def remove_column_duplicates(dataframe,column):
        # remove duplicates entries with the same Name, platform, genre
        dataframe.drop_duplicates(subset=column, inplace=True).reset_index(drop=True)
        return dataframe

    def standardize_text(dataframe,column):
        # return all entries of a column in string lower case/title/capitalize, based on the parameter format
        if dataframe[column].dtype != int:
            dataframe[column] = dataframe[column].str.lower()
            return dataframe
        else:
            print('Column is filled with integers\nAborting function')
            pass
        
    # def convert_types():
    #     # convert data types from x to y
    #     pass
    
    # Handling missing data
    
    def remove_na(dataframe,column):
        #remove rows with missing revelant data
        dataframe.dropna(subset=column,inplace=True)
        return dataframe

    def fill_na_median(dataframe,column):

        # fill empty values with median,mean,mode, whatever
        dataframe[column].fillna(value=dataframe[column].median(),inplace=True)
        return dataframe

    
    