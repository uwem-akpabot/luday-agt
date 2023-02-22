# Dockerfile
FROM python:3.7

WORKDIR /api/blogs

COPY requirements.txt /api/blogs/requirements.txt

RUN pip install -r requirements.txt

COPY . /api/blogs

ENTRYPOINT ["python"]
CMD ["run.py"]