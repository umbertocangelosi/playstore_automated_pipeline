from sqlalchemy import create_engine  
from sqlalchemy import Table, Column, String, MetaData, Integer, ForeignKey, Float
from sqlalchemy.orm import sessionmaker

class DbHandler():
    
    def __init__(self, url):
        '''
        Constructor for the DbHandler class
        
        Argomenti:
        - url: a string representing the URL for connecting to the database
        
        Creates an engine object to connect to the database and a metadata object to manage Table objects.
        '''
        self.engine = create_engine(url)
        self.metadata = MetaData()
        self.Session = sessionmaker(bind=self.engine)
        #self.session = self.Session
        self.Session.close_all()
        #self.connection = self.engine.connect()

    def create_table_google(self):

        with self.Session():
            table_name = 'google_play_store'
            existing_table = Table(table_name, self.metadata)
            existing_table.drop(self.engine, checkfirst=True)

        '''
        Creates a table if doesn't exist in the database
        '''
        with self.Session():
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
                extend_existing=True
            )
            print("Table google_play_store created!")
        
        self.metadata.create_all(bind=self.engine)


    def create_table_reviews(self):
        with self.Session():
            google_reviews = Table(
                'google_reviews', 
                self.metadata,
                Column('id', Integer(), autoincrement=True, primary_key=True),
                Column('app', String(255), ForeignKey("google_play_store.app"), nullable=False),
                Column('translated_review', String(255), nullable=False),
            )
            self.metadata.create_all(bind=self.engine)
            print("Table google_reviews created!")

    def create_score(self):
        with self.Session():

            score = Table(
                'google_score', 
                self.metadata,
                Column('app', String(255), ForeignKey("google_play_store.app"), nullable=False),
                Column('score', Float(), nullable=False),
            )
            self.metadata.create_all()
            print("Table google_reviews created!")

    def create_everything(self):

        self.create_table_google()
        self.create_table_reviews()
        self.create_score()
        