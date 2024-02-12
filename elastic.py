import os
import sys

os.environ['PYSPARK_PYTHON'] = 'python3.11'
os.environ['PYSPARK_DRIVER_PYTHON'] = 'python3.11'

import random
import string
from datetime import datetime, timedelta
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

spark = SparkSession.builder \
    .appName("DataFrame Example") \
    .master("spark://localhost:7077") \
    .getOrCreate()

SAMPLES = 100
data = [
    (
        datetime.now() - timedelta(days=random.randint(1, 10)),
        ''.join(random.choices(string.ascii_letters, k=10)),
        ''.join(random.choices(string.ascii_letters, k=10)),
        random.choice(["CARD", "CASH", "CRYPTO"]),
        random.randint(1, 100),
        random.choice(["USD", "EUR"]),
    )
    for _ in range(SAMPLES)
]
columns = ["Date", "Store", "Product", "Method", "Total", "Currency"]
df = spark.createDataFrame(data, schema=columns)

print("Original DataFrame:")
df.show()

filtered_df = df.filter(df.Total > 50)
print("Filtered DataFrame (Total > 50):")
filtered_df.show()

json_docs = df.toJSON().collect()
print("Elasticsearch document 1:", json_docs[0])
