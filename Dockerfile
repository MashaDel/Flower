FROM python:3

RUN apt-get update -y

RUN apt-get install tk -y

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["/app/app.py"]

ENTRYPOINT ["python3"]