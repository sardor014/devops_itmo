from datetime import datetime
from typing import List

from airflow.decorators import dag, task


class BinaryHeap:
    def __init__(self, init_arr: List[int] = None):
        self.heap = []
        self.heap_size = 0
        if init_arr is not None:
            for i in range(len(init_arr)):
                print(self.heap)
                self.add(init_arr[i])

    def __call__(self) -> List[int]:
        return self.heap

    def swap(self, i: int, j: int) -> None:
        dummy = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = dummy

    def sift_up(self, i: int) -> None:
        while i >= 1 and self.heap[i] < self.heap[(i - 1) // 2]:
            self.swap(i, (i - 1) // 2)
            i = (i - 1) // 2

    def sift_down(self, i: int) -> None:
        while 2 * i + 1 < self.heap_size:
            left = 2 * i + 1
            right = 2 * i + 2
            j = left
            if right < self.heap_size and self.heap[right] < self.heap[left]:
                j = right

            if self.heap[i] <= self.heap[j]:
                break

            self.swap(i, j)
            i = j

    def add(self, val: int) -> None:
        self.heap_size += 1
        self.heap.append(val)
        self.sift_up(self.heap_size - 1)

    def extract_min(self) -> int:
        min_elem = self.heap[0]
        self.heap[0] = self.heap[self.heap_size - 1]
        self.heap.pop(self.heap_size - 1)
        self.heap_size -= 1
        self.sift_down(0)

        return min_elem


@dag(
    dag_id="factorial",
    start_date=datetime(2026, 1, 1),
)
def factorial() -> None:
    @task
    def get_numbers() -> List[int]:
        return [12, 5, 9, 3, 14, 8, 6, 11, 22, 10, 7, 4, 15, 11, 13, 16, 18, 17, 20, 19]

    @task
    def extract_minimum(numbers: List[int]) -> int:
        heap = BinaryHeap(numbers)
        min_number = heap.extract_min()
        print(f"Heap after initialization: {heap()}")
        print(f"Minimum number: {min_number}")
        return min_number

    @task
    def calculate_factorial(number: int) -> int:
        result = 1
        for value in range(2, number + 1):
            result *= value
        return result

    @task
    def print_result(number: int, factorial: int) -> None:
        print(f"Factorial of minimum number {number} is {factorial}")

    numbers = get_numbers()
    min_number = extract_minimum(numbers)
    factorial_result = calculate_factorial(min_number)
    print_result(min_number, factorial_result)


factorial()
