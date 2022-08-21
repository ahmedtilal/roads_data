FROM apache/airflow:2.3.3-python3.10

LABEL maintainer="ahmedtilal1@gmail.com"

ENV AIRFLOW_HOME=/opt/airflow
ENV FERNET_KEY=${AIRFLOW__CORE__FERNET_KEY}

USER airflow

WORKDIR ${AIRFLOW_HOME}

COPY --chown=airflow:root ./requirements.txt .

RUN pip install -r requirements.txt

# COPY Pipfile* ${AIRFLOW_HOME}
 
# RUN pipenv install --system --deploy

COPY --chown=airflow:root ./dags ${AIRFLOW_HOME}