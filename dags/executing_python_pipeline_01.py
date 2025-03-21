import pandas as pd

from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


default_args = {
   'owner': 'loonycorn'
}

def read_csv_file():
    df = pd.read_csv('/home/opanggam/airflow/datasets/insurance.csv')

    print(df)

    return df.to_json()


with DAG(
    'python_pipeline',
    description='Running a Python pipeline',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval='@once',
    tags = ['python', 'transform', 'pipeline']
) as dag:
    read_csv_file = PythonOperator(
        task_id='read_csv_file',
        python_callable=read_csv_file
    )

read_csv_file