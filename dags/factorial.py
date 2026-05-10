from datetime import datetime

from airflow.decorators import dag, task


@dag(
    dag_id="factorial",
    start_date=datetime(2026, 1, 1),
)
def factorial() -> None:
    @task
    def get_number() -> int:
        return 7

    @task
    def calculate_factorial(number: int) -> int:
        result = 1
        for value in range(2, number + 1):
            result *= value
        return result

    @task
    def print_result(number: int, factorial: int) -> None:
        print(f"Factorial of {number} is {factorial}")

    number = get_number()
    factorial = calculate_factorial(number)
    print_result(number, factorial)


factorial()
