# Changes

### Лаб. 1-2
- Добавлены сервисы `spark-master` и `spark-worker` в `docker-compose.yml`
- В `Dockerfile` добавлена установка `procps`, `default-jre` и `apache-airflow-providers-apache-spark`
- Добавлена папка `spark`
- Добавлен DAG `spark_factorial`, который запускает Spark job через `SparkSubmitOperator`

### Лаб. 3
- Настроен локальный self-hosted runner в GitHub Actions с тегом `my-custom-runner`
- Создан файл конфигурации пайплайна `.github/workflows/cicd.yml`
- Добавлен стейдж `test`, проверяющий наличие директорий `dags/` и `spark/` (настроен на запуск во всех ветках; прерывает пайплайн в случае отсутствия папок)
- Добавлен стейдж `build` для автоматической сборки Docker-образа (настроено правило пропуска для веток с префиксом `feature/`)
- Добавлен стейдж `deploy` для развертывания приложения (настроено правило: автоматический деплой осуществляется только для веток `main`, `master` и `develop`)