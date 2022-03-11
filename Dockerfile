FROM python:3.8-slim
WORKDIR /opt/server
COPY app/ .
COPY app/worker /worker
COPY app/redis-app /redis/
ENV WORKER=worker/worker.py
ENV REDIS=redis
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN apt-get update
RUN apt-get -y install libpq-dev gcc
RUN pip install -r requirements.txt
CMD ["python","app.py"]