FROM python:3.9-alpine
WORKDIR /usr/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add postgresql-dev gcc python3-dev musl-dev && \
    pip install --upgrade pip

COPY ./requirements ./requirements
RUN pip install -r requirements/production.txt

COPY ./entrypoint.sh .

COPY . .

EXPOSE 8001

# run entrypoint.sh
ENTRYPOINT ["/usr/app/entrypoint.sh"]

CMD gunicorn --bind 0.0.0.0:8001 config.wsgi:application