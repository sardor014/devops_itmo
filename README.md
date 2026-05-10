# DAG factorial

DAG строит бинарную кучу из массива на 20 элементов, извлекает минимальное значение и считает факториал этого минимума

Массив:

```text
[12, 5, 9, 3, 14, 8, 6, 11, 20, 10, 7, 4, 15, 19, 13, 16, 18, 17, 21, 22]
```

DAG состоит из четырех задач:

1. `get_numbers` - возвращает массив чисел
2. `extract_minimum` - добавляет элементы в бинарную кучу и извлекает минимум
3. `calculate_factorial` - считает факториал найденного минимума
4. `print_result` - выводит результат в лог Airflow

Результат выполнения:

```text
Factorial of minimum number 3 is 6
```

# Локальный запуск

Создать файл `.env`:

```env
AIRFLOW_UID=1000
```

Запустить сервисы:

```bash
docker compose up -d --build
```

Открыть Airflow:

```text
http://localhost:8080
```

Логин и пароль:

```text
airflow / airflow
```

После входа нужно найти DAG `factorial`, включить его и запустить вручную через `Trigger DAG`

# Остановка

```bash
docker compose down
```
