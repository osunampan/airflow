from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'admin',
}

with DAG(
    dag_id='executing_multiple_tasks',
    description='Executing Multiple Tasks',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval='@once' # @once is useful for manual 
) as dag:

    task1 = BashOperator(
        task_id='task_1',
        bash_command='echo - Task 1 is executed',
    )

    task2 = BashOperator(
        task_id='task_2',
        bash_command='echo - Task 2 is executed',
    )

task1.set_downstream(task2)