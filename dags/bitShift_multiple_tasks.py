from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'admin',
}

with DAG( 
    dag_id='bitshift_multiple_tasks',
    description='Executing Multiple Tasks using bitshift',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval=timedelta(days=1),
    tags = ['upstream', 'downstream'],

) as dag:

    task1 = BashOperator(
        task_id='task_1',
        bash_command='''
        echo - Task 1 is executed
        for i in {1....10}
        do
            echo Task 1 printing $i
        done

        echo Task 1 has ended!
        '''
    )

    task2 = BashOperator(
        task_id='task_2',
        bash_command='''
        echo - Task 2 is executed
        sleep 4
        echo Task 2 has ended
        '''
    )

    task3 = BashOperator(
        task_id='task_3',
        bash_command='''
        echo - Task 3 is executed
        sleep 15
        echo Task 3 has ended
        '''
    )

    task4 = BashOperator(
        task_id = 'task_4',
        bash_command='echo Task 4 is completed!'
    )

task1 >> task2 # downstream
task1 >> task3 

task4 << task2 
task4 << task3 # upstream

## above can also be written as 
# task1 >> [task2, task3]
# task4 << [task2, task3]