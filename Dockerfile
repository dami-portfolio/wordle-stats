FROM apache/airflow:latest-python3.9

WORKDIR /app
COPY . /app

CMD [ "python", "wordle_stats.py"]

