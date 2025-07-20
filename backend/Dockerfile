FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install flask

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
