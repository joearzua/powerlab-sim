FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install requests

CMD ["python", "device_simulator.py"]
