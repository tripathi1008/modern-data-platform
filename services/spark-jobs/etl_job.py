print("Running ETL pipeline")
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ETL").getOrCreate()

df = spark.read.csv("data/customers.csv", header=True)

df.show()