import os
import sys
from pyspark.sql import SparkSession

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

spark = SparkSession.builder \
    .appName("VSCodeTest") \
    .master("local[*]") \
    .getOrCreate()

df = spark.createDataFrame([("Alice", 25), ("Bob", 30)])
df.show()

spark.stop()