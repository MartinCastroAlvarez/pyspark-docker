import os
import sys

os.environ['PYSPARK_PYTHON'] = 'python3.11'
os.environ['PYSPARK_DRIVER_PYTHON'] = 'python3.11'

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("My PySpark Job") \
    .master("spark://localhost:7077") \
    .getOrCreate()

SAMPLES = 100000

def inside(p):
    import random
    x, y = random.random(), random.random()
    return x*x + y*y < 1

count = spark.sparkContext.parallelize(range(0, SAMPLES)) \
         .filter(inside).count()

print("Pi is roughly %f" % (4.0 * count / SAMPLES))

spark.stop()
