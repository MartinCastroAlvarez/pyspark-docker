FROM bitnami/spark:latest

USER root

RUN apt-get update
RUN apt-get install -y wget
RUN wget https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tgz
RUN tar xzf Python-3.8.3.tgz
RUN apt-get install -y build-essential checkinstall
RUN apt-get install -y libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
RUN cd Python-3.8.3 && ./configure --enable-optimizations && make altinstall

USER 1001
