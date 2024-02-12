# pyspark-hdfs-docker
Running PySpark jobs using Docker

![wallpaper.jpg](wallpaper.jpg)

Apache Spark is an open-source, distributed computing system that offers a comprehensive framework for handling big data processing and analytics. Spark provides high-level APIs in Java, Scala, Python, and R, making it accessible to a wide range of developers and data scientists. It is designed to perform both batch processing and real-time data processing efficiently. Spark achieves high performance for both streaming and batch data using a DAG (Directed Acyclic Graph) scheduler, a query optimizer, and a physical execution engine. At its core, Spark facilitates the development of complex data pipelines and iterative algorithms, while its in-memory computing capabilities allow it to process large datasets quickly. Spark's ecosystem includes several libraries for diverse tasks like SQL and DataFrames, machine learning (MLlib), graph processing (GraphX), and stream processing (Spark Streaming), making it a versatile tool for big data analytics and machine learning projects.

PySpark is the Python API for Apache Spark, allowing Python programmers to leverage the capabilities of Spark using Python's rich ecosystem. It provides a way to interface with Spark's distributed computing capabilities, enabling data scientists and analysts to execute data analysis and machine learning tasks at scale. PySpark offers Python wrappers for Spark's distributed data collections (RDDs and DataFrames) and its powerful APIs for streaming, SQL, machine learning, and graph processing. This seamless integration with Python enables users to combine the simplicity and flexibility of Python with the power of Apache Spark to analyze big data and derive insights. PySpark has become particularly popular in the data science community, where Python is widely used, as it allows for easy development of scalable and complex data pipelines and algorithms, all within the Python environment.

## Instructions

* Build Docker image:

```bash
docker build -t sparky:latest .
```

* Create a docker network:

```bash
docker network create sparky
```

* Run Spark master container:

```bash
docker rm spark-master
docker run --name spark-master \
    -e SPARK_MODE=master \
    -e PYSPARK_PYTHON=python3.11 \
    -e PYSPARK_DRIVER_PYTHON=python3.11 \
    -p 8080:8080 -p 8081:8081 -p 7077:7077 \
    --network sparky \
    sparky:latest
```

* Run Spark worker container:

```bash
docker rm spark-worker-1
docker run --name spark-worker-1 \
    -e SPARK_MODE=worker \
    -e PYSPARK_PYTHON=python3.11 \
    -e PYSPARK_DRIVER_PYTHON=python3.11 \
    -e SPARK_MASTER_URL=spark://spark-master:7077 \
    --network sparky \
    sparky:latest
```

* Visit [http://localhost:8080](http://localhost:8080).

* Install Python dependencies:

```bash
virtualenv -p python3.11 .env
source .env/bin/activate
pip install -r requirements.txt
```

* Calculate `pi` using PySpark:

```bash
python3.11 pi.py
```
```bash
Pi is roughly 3.134520                                                          
```

* Calculate average age of 

```bash
python3.11 filter.py
```
```bash
Average Age of People Older Than 25:
+------------------+
|          avg(Age)|
+------------------+
|62.036144578313255|
+------------------+
```

* Generate a dataset for Elasticsearch:

```bash
python3.11 elastic.py
```
```bash
Elasticsearch document 1: {"Date":"2024-02-06T22:07:43.129-03:00","Store":"LJbQxEXVhR","Product":"HrSQpQofYw","Method":"CASH","Total":37,"Currency":"USD"}
```
