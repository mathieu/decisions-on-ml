FROM python:3.5.3

WORKDIR /app/

COPY requirements.txt /app/
RUN pip install -r ./requirements.txt

COPY main.py __init__.py /app/

COPY data/miniloan-decisions-default-1K.csv /app/data/

COPY models/miniloandefault-svc.joblist /app/models/

# ENTRYPOINT /bin/bash
EXPOSE 5000

ENV ENVIRONMENT local

ENTRYPOINT python ./main.py