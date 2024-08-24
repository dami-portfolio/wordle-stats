FROM apache/airflow:latest-python3.9

WORKDIR /app
COPY . /app

CMD [ "python3", "wordle_stats.py"]

