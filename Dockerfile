FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y libpq-dev gcc netcat libmagic-dev cron

RUN mkdir /app -p
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app/
RUN chmod +x /app/scripts/entrypoint.sh
ENTRYPOINT ["/app/scripts/entrypoint.sh"]
