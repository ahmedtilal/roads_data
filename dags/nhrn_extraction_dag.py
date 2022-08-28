import pendulum
from typing import List
from airflow.decorators import dag, task
from airflow.providers.docker.operators.docker import DockerOperator


@dag(
    schedule_interval=None,
    start_date=pendulum.datetime(2021, 7, 15, tz="UTC"),
    catchup=False,
    tags=["iteration_1"],
)
def nhrn_etl():
    """
    ### National Highways and Roads Network ETL Pipeline

    This DAG downloads CSV files from the NHRN page for planned road works data in the data.gov website, and saves the ingested data in the database.

    First, we scrape the website to check if there are any new files uploaded that we haven't ingested. Then, if a new file is present we pass it on to the ingestion dags to download it and save its contents to the database.

    """

    get_current_links = DockerOperator(
        task_id='get_current_links',
        image='selenium-scraper:latest',
        shm_size='2gb',
        api_version='auto',
        auto_remove=True,
        docker_url='tcp://docker-proxy:2375',
    )


    @task()
    def transform():
        """
        #### Transform task
        """

        return True

    @task()
    def load_data(total_order_value: float):
        """
        #### Load task
        """

        print(f"Total order value is: {total_order_value:.2f}")

    get_current_links >> transform() >> load_data(99.5)


nhrn_extraction_dag = nhrn_etl()
