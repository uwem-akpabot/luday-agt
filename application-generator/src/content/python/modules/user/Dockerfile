# Dockerfile
FROM python:3.7

WORKDIR /api/user

COPY requirements.txt /api/user/requirements.txt

RUN pip install -r requirements.txt

COPY . /api/user

ENTRYPOINT ["python"]

CMD ["run.py"]