FROM python:3.9

WORKDIR /app
COPY . /app

RUN pip install torch mlflow

CMD ["python", "model/train.py"]
