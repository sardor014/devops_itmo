# Changes

- Добавлены сервисы `spark-master` и `spark-worker` в `docker-compose.yml`
- В `Dockerfile` добавлена установка `procps`, `default-jre` и `apache-airflow-providers-apache-spark`
- Добавлена папка `spark`
- Добавлен DAG `spark_factorial`, который запускает Spark job через `SparkSubmitOperator`
s