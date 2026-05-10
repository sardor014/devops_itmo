from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession


conf = SparkConf().setAppName("Spark Factorial Job").setMaster("spark://spark-master:7077")
sc = SparkContext(conf=conf)

spark = SparkSession.builder.config(conf=conf).getOrCreate()

numbers = [12, 5, 9, 3, 14, 8, 6, 11, 22, 10, 7, 4, 15, 11, 13, 16, 18, 17, 20, 19]
values = ", ".join(f"({number})" for number in numbers)

minimum = spark.sql(f"SELECT MIN(number) AS minimum FROM VALUES {values} AS numbers(number)").collect()[0][
    "minimum"
]

factorial = 1
for value in range(2, minimum + 1):
    factorial *= value

print(f"Minimum number: {minimum}")
print(f"Factorial of minimum number {minimum} is {factorial}")

spark.stop()
