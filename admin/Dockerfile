FROM python:3.9

ENV PYTHONPATH "${PYTHONPATH}:/app/"
ENV PATH="${PATH}:/root/.local/bin"

RUN apt update && apt -y upgrade && apt install -y netcat postgresql-client python3-setuptools && pip install pipenv

RUN mkdir /app
WORKDIR /app/
COPY Pipfile/ /app/
COPY Pipfile.lock/ /app/
RUN pipenv install --system --deploy --skip-lock

ENTRYPOINT [ "/opt/app/entrypoint.sh" ]
