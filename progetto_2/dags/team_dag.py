from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import psycopg2
from sqlalchemy import create_engine

from src.DataIngestor import DataIngestor
from src.DataCleaner import DataCleaner
from src.DataVisualizer import DataVisualizer
from src.DataAnalyser import DataAnalyser

di = DataIngestor()
dc = DataCleaner()
da = DataAnalyser()
dv = DataVisualizer()


default_dag_args = {
    'start_date': datetime(2023, 2, 14),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'project_id': 1
}

def load_google():
    pass
def load_reviews():
    pass
def clean_google():
    pass
def clean_reviews():
    pass
def connect():
    pass
def create_google():
    pass
def create_reviews():
    pass
def save_google():
    pass
def save_reviews():
    pass
def analyse():
    pass
def create_score():
    pass
def save_score():
    pass

# define dag
with DAG("main_dag", schedule_interval = '@once', catchup = False, default_args = default_dag_args) as dag:

    # define tasks of the dag
    task_1 = PythonOperator(task_id = 'load_google', python_callable = di.read_file("./progetto_2/data/raw/googleplaystore.csv"))
    task_2 = PythonOperator(task_id = 'load_reviews', python_callable = di.read_file('./progetto_2/data/raw/googleplaystore_user_reviews.csv'))
    task_3 = PythonOperator(task_id = 'clean_google', python_callable = dc.clean_google(google_data))
    task_4 = PythonOperator(task_id = 'clean_reviews', python_callable = clean_reviews)
    task_5 = PythonOperator(task_id = 'connect', python_callable = connect)
    task_6 = PythonOperator(task_id = 'create_google', python_callable = create_google)
    task_7 = PythonOperator(task_id = 'create_reviews', python_callable = create_reviews)
    task_8 = PythonOperator(task_id = 'save_google', python_callable = save_google)
    task_9 = PythonOperator(task_id = 'save_reviews', python_callable = save_reviews)
    task_10 = PythonOperator(task_id = 'analyse', python_callable = analyse)
    task_11 = PythonOperator(task_id = 'create_score', python_callable = create_score)
    task_12 = PythonOperator(task_id = 'save_score', python_callable = save_score)

task_1 >> task_2 >> task_3 >> task_4 >> task_5 >> task_6 >> task_7 >> task_8 >> task_9 >> task_10 >> task_11 >> task_12