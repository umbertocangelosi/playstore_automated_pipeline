# print(df['Size'][df['Size'] != 'Varies with device'][~df['Size'].str.contains('M')][~df['Size'].str.contains('k')])
class DataCleaner:
    def __init__(self):
        pass
    
    def to_number(self, dataframe,column):
        
        # leave only numbers and dots, then cast to int64
        dataframe = dataframe.assign(column = pd.to_numeric(df[column].str.replace('[^0-9.]', '')))
        return dataframe

    def comma_to_dot():
        # replace commas with dots
        pass

    def size_to_number():
        # replace (M with '000',k with '',G with '000000')
        pass

    # se ha senso si fa anche questa, altrimenti no

    def convert_date():
        # convert date from string to date
        pass