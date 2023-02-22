# Dockerfile
FROM python:3.7

WORKDIR /api/contact

COPY requirements.txt /api/contact/requirements.txt

RUN pip install -r requirements.txt

COPY . /api/contact

ENTRYPOINT ["python"]

CMD ["run.py"]