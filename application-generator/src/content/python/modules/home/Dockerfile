# Dockerfile
FROM python:3.7

WORKDIR /api/home

COPY requirements.txt /api/home/requirements.txt

RUN pip install -r requirements.txt

COPY . /api/home

ENTRYPOINT ["python"]

CMD ["run.py"]