from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import min as spark_min


conf = SparkConf().setAppName("Spark Factorial Job").setMaster("spark://spark-master:7077")
sc = SparkContext(conf=conf)

spark = SparkSession.builder.config(conf=conf).getOrCreate()

numbers = [12, 5, 9, 3, 14, 8, 6, 11, 22, 10, 7, 4, 15, 11, 13, 16, 18, 17, 20, 19]
numbers_df = spark.createDataFrame([(number,) for number in numbers], ["number"])

minimum = numbers_df.select(spark_min("number").alias("minimum")).collect()[0]["minimum"]

factorial = 1
for value in range(2, minimum + 1):
    factorial *= value

print(f"Minimum number: {minimum}")
print(f"Factorial of minimum number {minimum} is {factorial}")

spark.stop()
