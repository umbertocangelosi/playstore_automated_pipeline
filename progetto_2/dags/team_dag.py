from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from sqlalchemy import create_engine
import pandas as pd
import sys
import os

sys.path.append('/mnt/c/Users/Alessio/Desktop/Team/progetto_2')

from src.DataIngestor import DataIngestor
from src.DataCleaner import DataCleaner
from src.DataVisualizer import DataVisualizer
from src.DataAnalyser import DataAnalyser
from src.DbHandler import DbHandler

di = DataIngestor()
dc = DataCleaner()
da = DataAnalyser()
dv = DataVisualizer()
dbh = DbHandler('postgresql://postgres:postgres@localhost:5432/postgres')
#dbh = DbHandler('postgresql://onyhtqzn:ej-TLeomNZACBDKE7_PhUfZmCSUcFRW1@surus.db.elephantsql.com/onyhtqzn')

default_dag_args = {
    'start_date': datetime(2023, 4, 15),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
    'project_id': 1
}

def import_app(**context):
    path = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'googleplaystore.csv')
    # import dataframe 
    google_data = di.read_file(path)
    # save dataframe using XCom
    context['ti'].xcom_push(key='google', value=google_data.to_dict(orient='records'))

def clean_app(**context):

    # getting dataframe from Context
    google_data = context['ti'].xcom_pull(key='google')
    google_data = pd.DataFrame.from_dict(google_data)
    # cleaning dataframe using DataCleaner Class
    google_data = dc.clean_google(google_data)
    # save dataframe using XCom
    context['ti'].xcom_push(key='google', value=google_data.to_dict(orient='records'))

def import_review(**context):

    path = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'googleplaystore_user_reviews.csv')
    # import dataframe
    google_reviews = di.read_file(path)
    # save dataframe using XCom
    context['ti'].xcom_push(key='reviews', value=google_reviews.to_dict(orient='records'))

def clean_review(**context):
    path_p = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'p.xlsx')
    path_n = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'n.xlsx')
    # getting dataframe from Context
    google_data = context['ti'].xcom_pull(key='google')
    google_data = pd.DataFrame.from_dict(google_data)
    google_reviews = context['ti'].xcom_pull(key='reviews')
    google_reviews = pd.DataFrame.from_dict(google_reviews)
    positive = di.read_file(path_p)
    negative = di.read_file(path_n)
    final_list = dc.clean_sentiment_list(positive,negative)
    # cleaning dataframe using DataCleaner Class
    google_reviews = dc.clean_google_reviews(google_reviews, google_data)
    analysed_review = dc.replace_common_strings(google_reviews,'translated_review',final_list)
    # save dataframe using XCom
    context['ti'].xcom_push(key='reviews', value=google_reviews.to_dict(orient='records'))
    context['ti'].xcom_push(key='analysed_review', value=analysed_review.to_dict(orient='records'))


def create_tabs():
    dbh.create_tables()
    
def export_app(**context):
    # save app dataframe on database
    google_data = context['ti'].xcom_pull(key='google')
    google_data = pd.DataFrame.from_dict(google_data)
    dbh.to_cloud(google_data, to_table='store')
    path = os.path.join(os.path.dirname(__file__), '..', 'data', 'output', 'google_cleaned.csv')
    di.save_file(google_data, path)

def export_review(**context):
    # save review dataframe on database
    google_reviews = context['ti'].xcom_pull(key='reviews')
    google_reviews = pd.DataFrame.from_dict(google_reviews)
    dbh.to_cloud(google_reviews, to_table='review')
    path = os.path.join(os.path.dirname(__file__), '..', 'data', 'output', 'reviews_cleaned.csv')
    di.save_file(google_reviews, path)
   
def analysis(**context):
    # getting app and reviews dataframe
    google_data = context['ti'].xcom_pull(key='google')
    google_data = pd.DataFrame.from_dict(google_data)
    analysed_review = context['ti'].xcom_pull(key='analysed_review')
    analysed_review = pd.DataFrame.from_dict(analysed_review)
    # running analysis
    sentiment = da.assign_sentiment(google_data, analysed_review)
    context['ti'].xcom_push(key='analysis', value=sentiment.to_dict(orient='records'))

def export_analysis(**context):

    sentiment = context['ti'].xcom_pull(key='analysis')
    sentiment = pd.DataFrame.from_dict(sentiment)
    dbh.to_cloud(sentiment, to_table='score')
    path = os.path.join(os.path.dirname(__file__), '..', 'data', 'output', 'analysis.csv')
    di.save_file(sentiment, path)

# Define the DAG

with DAG('etl_main', default_args=default_dag_args, schedule_interval=None) as dag:

# Define the operators
    import_app_task = PythonOperator(task_id='import_app_task',
                            python_callable=import_app,
                            provide_context=True)
    
    clean_app_task = PythonOperator(task_id='clean_app_task',
                            python_callable=clean_app,
                            provide_context=True)
    
    import_review_task = PythonOperator(task_id='import_reviews_task',
                            python_callable=import_review,
                            provide_context=True)
    
    clean_review_task = PythonOperator(task_id='clean_review_task',
                            python_callable=clean_review,
                            provide_context=True)
    
    create_tabs_task = PythonOperator(task_id='create_tabs_task',
                            python_callable=create_tabs,
                            provide_context=True)
    
    export_app_task = PythonOperator(task_id='export_app_task',
                            python_callable=export_app,
                            provide_context=True)
    
    export_review_task = PythonOperator(task_id='export_review_task',
                            python_callable=export_review,
                            provide_context=True)
    
    analysis_task = PythonOperator(task_id='analysis_task',
                            python_callable=analysis,
                            provide_context=True)
    
    export_analysis_task = PythonOperator(task_id='export_analysis_task',
                             python_callable=export_analysis,
                             provide_context=True)

# Define the task dependencies
create_tabs_task >> import_app_task >> import_review_task >> \
clean_app_task >> clean_review_task >> export_app_task >> export_review_task >> \
analysis_task >> export_analysis_task