from sqlalchemy import create_engine  
from sqlalchemy import Table, Column, String, MetaData, Integer, ForeignKey, Float

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

    def create_table_google(self):
        '''
        Creates a table if doesn't exist in the database
        '''
        google_play_store = Table(
            'google_play_store', 
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
            Column('last_updated', String(255), nullable=False),
        )
        print("Table google_play_store created!")


    def create_table_reviews(self):

        google_reviews = Table(
            'google_reviews', 
            self.metadata,
            Column('id', Integer(), autoincrement=True, primary_key=True),
            Column('app', String(255), ForeignKey("google_play_store.app"), nullable=False),
            Column('translated_review', String(255), nullable=False),
        )
        print("Table google_reviews created!")

    def create_score(self):

        score = Table(
            'google_score', 
            self.metadata,
            Column('app', String(255), ForeignKey("google_play_store.app"), nullable=False),
            Column('score', Float(), nullable=False),
        )
        print("Table google_reviews created!")

    def create_everything(self):

        self.create_table_google()
        self.create_table_reviews()
        self.create_score()
        print('SIAMO ALLA FINE')
        self.metadata.create_all()