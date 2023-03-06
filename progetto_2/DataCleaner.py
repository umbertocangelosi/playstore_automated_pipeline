# print(df['Size'][df['Size'] != 'Varies with device'][~df['Size'].str.contains('M')[~df['Size'].str.contains('k')])

class DataProcessing:
    
    def __init__(self):
        pass
    
    # why this is not working ?
    def to_number(self, dataframe,column):        
        # leave only numbers and dots, then cast to int64
        dataframe = dataframe.assign(column = pd.to_numeric(df[column].str.replace('[^0-9.]', '')))
        return dataframe

    def comma_to_dot():
        # replace commas with dots
        pass

    def size_to_number():
        # replace (M with '000',k with '',G with '000000'). output in mega
        pass

    # se ha senso si fa anche questa, altrimenti no

    def convert_date():
        # convert date from string to date
        pass
    
    def remove_duplicates():
        # remove duplicates entries with the same Name, platform, genre
        pass
    
    def standardize_text(format=('l','t','c')):
        # return all entries of a column in string lower case/title/capitalize, based on the parameter format
        pass
    
    def convert_types():
        # convert data types from x to y
        pass
    
    # Handling missing data
    
    def remove_na():
        #remove rows with missing revelant data
        pass
    def fill_na():
        # fill empty values with median,mean,mode, whatever
        pass
    
    # drop column?
    
    