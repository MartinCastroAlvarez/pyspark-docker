import os
import sys

os.environ['PYSPARK_PYTHON'] = 'python3.11'
os.environ['PYSPARK_DRIVER_PYTHON'] = 'python3.11'

import random
import string
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

spark = SparkSession.builder \
    .appName("DataFrame Example") \
    .master("spark://localhost:7077") \
    .getOrCreate()

SAMPLES = 100
data = [
    (
        ''.join(random.choices(string.ascii_letters, k=10)),
        random.randint(1, 100),
    )
    for _ in range(SAMPLES)
]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, schema=columns)

print("Original DataFrame:")
df.show()

filtered_df = df.filter(df.Age > 25)
print("Filtered DataFrame (Age > 25):")
filtered_df.show()

avg_age = filtered_df.select(avg("Age"))
print("Average Age of People Older Than 25:")
avg_age.show()

spark.stop()
