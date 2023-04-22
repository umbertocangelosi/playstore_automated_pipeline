from sqlalchemy import create_engine  
from sqlalchemy import Table, Column, String, MetaData, Integer, ForeignKey, Float, Text
import pandas as pd

class DbHandler():
    
    def __init__(self, url):
        '''
        Constructor for the DbHandler class
        
        Args:
        - url: a string representing the URL for connecting to the database
        
        Creates an engine, connection and metadata object based on the url given
        '''
        self.engine = create_engine(url)
        self.metadata = MetaData(bind=self.engine)
        self.connection = self.engine.connect()

    def create_table_google(self):
        """
        Creates a table in the external database for Google Play Store data.

        The table will contain information about the app, including the name, category, rating, number of reviews,
        size, number of installs, type, price, content rating, and genre.

        Takes no input and returns nothing.
        """
        google_play_store = Table(
            'store', 
            self.metadata,
            Column('app', String(255), primary_key=True, nullable=False),
            Column('category', String(255), nullable=False),
            Column('rating', Float(), nullable=False),
            Column('reviews', Integer(), nullable=False),
            Column('size', Integer(), nullable=False),
            Column('installs', Integer(), nullable=False),
            Column('type', String(255), nullable=False),
            Column('price', Float(), nullable=False),
            Column('content_rating', String(255), nullable=False),
            Column('genres', String(255), nullable=False),
        )
        print("Table store created!")


    def create_table_reviews(self):
        """
        Creates a table in the external database for Google Play Store reviews.

        The table will contain reviews for each app, including the app ID, the translated review, and a unique ID 
        for each review.

        The app ID is a foreign key referencing the app table.

        Takes no input and returns nothing.
        """
        google_reviews = Table(
            'review', 
            self.metadata,
            Column('id', Integer(), autoincrement=True, primary_key=True),
            Column('app', String(255), ForeignKey("store.app"), nullable=False),
            Column('translated_review', Text(), nullable=False),
        )
        print("Table review created!")

    def create_score(self):
        """
        Creates a table in the external database for Google Play Store app scores.

        The table will contain scores for each app, including the app ID and the score.

        The app ID is a foreign key referencing the app table, and is also the primary key for the score table.

        Takes no input and returns nothing.
        """
        score = Table(
            'score', 
            self.metadata,
            Column('app', String(255), ForeignKey("store.app"), primary_key=True, nullable=False),
            Column('score', Float(), nullable=False),
        )
        print("Table review created!")

    def create_tables(self):
        """
        Creates or updates tables in the external database for Google Play Store data.

        First checks if the 'store' table already exists in the database. If it does, all existing tables
        (including 'store', 'review', and 'score') are deleted. If it does not exist, the function creates
        the 'store', 'review', and 'score' tables using the respective create_table functions.

        After creating or updating the tables, the function commits the changes to the database.

        Takes no input and returns nothing.
        """
        if self.connection.dialect.has_table(connection=self.connection, table_name='store'):
            print('\nDeleting all the tables\n')
            self.connection.execute('DROP TABLE if exists store CASCADE')
            self.connection.execute('DROP TABLE if exists review CASCADE')
            self.connection.execute('DROP TABLE if exists score CASCADE')
        self.create_table_google()
        self.create_table_reviews()
        self.create_score()
        self.metadata.create_all()

    def to_cloud(self, dataframe, to_table):
        """
        Uploads a Pandas DataFrame to a SQL table in the cloud.

        Args:
            dataframe (pandas.DataFrame): The DataFrame to upload.
            to_table (str): The name of the table to create or update.

        Returns:
            None.
        """
        dataframe.to_sql(name=to_table, con=self.connection, if_exists='append', index=False)
        print(f"\n{dataframe} has been successfully uploaded!\n")

    def from_cloud(self, table):
        """
        This function reads a table from the connected cloud database and returns it as a pandas DataFrame.

        Args:
        table (str): The name of the table to read from the database.

        Returns:
        pandas.DataFrame: A DataFrame containing the data from the specified table.
        """
        table = pd.read_sql(f'select * from "{table}"', self.connection)
        print(f'{table} has been loaded from our database online')
        return table