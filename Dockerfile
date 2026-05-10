FROM apache/airflow:2.7.1

WORKDIR /opt/airflow

USER root
RUN apt update && apt -y install procps default-jre

USER airflow
COPY ./dags ./dags
COPY ./spark ./spark
RUN pip3 install apache-airflow-providers-apache-spark==4.4.0
