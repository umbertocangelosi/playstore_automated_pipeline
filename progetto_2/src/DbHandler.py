from sqlalchemy import create_engine  
from sqlalchemy import Table, Column, String, MetaData, Integer, ForeignKey, Float, Text
import pandas as pd

class DbHandler():
    
    def __init__(self, url):
        '''
        Constructor for the DbHandler class
        
        Argomenti:
        - url: a string representing the URL for connecting to the database
        
        Creates an engine object to connect to the database and a metadata object to manage Table objects.
        '''
        self.engine = create_engine(url)
        self.metadata = MetaData(bind=self.engine)
        self.connection = self.engine.connect()

    def create_table_google(self):
        '''
        Creates a table if doesn't exist in the database
        '''
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

        google_reviews = Table(
            'review', 
            self.metadata,
            Column('id', Integer(), autoincrement=True, primary_key=True),
            Column('app', String(255), ForeignKey("store.app"), nullable=False),
            Column('translated_review', Text(), nullable=False),
        )
        print("Table review created!")

    def create_score(self):

        score = Table(
            'score', 
            self.metadata,
            Column('app', String(255), ForeignKey("store.app"), nullable=False),
            Column('score', Float(), nullable=False),
        )
        print("Table review created!")

    def create_tables(self):
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
        # dataframe : what we are pushing
        # to_table : table we are pushing to
        dataframe.to_sql(name=to_table, con=self.connection, if_exists='append', index=False)
        print(f"\n{dataframe} has been successfully uploaded!\n")

    def from_cloud(self, table):
        table = pd.read_sql(f'select * from "{table}"', self.connection)
        print(f'{table} has been loaded from our database online')
        return table