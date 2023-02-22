# Dockerfile
FROM python:3.7

WORKDIR /api/emails

COPY requirements.txt /api/emails/requirements.txt

RUN pip install -r requirements.txt

COPY . /api/emails

ENTRYPOINT ["python"]

CMD ["run.py"]