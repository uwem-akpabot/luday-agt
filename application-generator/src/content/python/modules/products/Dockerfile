# Dockerfile
FROM python:3.7

WORKDIR /api/products

COPY requirements.txt /api/products/requirements.txt

RUN pip install -r requirements.txt

COPY . /api/products

ENTRYPOINT ["python"]

CMD ["run.py"]