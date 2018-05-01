FROM python:3.6-jessie
Add . /code
WORKDIR /code
RUN pip install -r requirements.txt
WORKDIR /code/src/endpoints
# CMD ["gunicorn", "main:application", "--bind", "localhost:8080", "--worker-class", "aiohttp.GunicornWebWorker"]
CMD ["python3", "main.py"]