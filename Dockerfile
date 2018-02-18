FROM python:3.6-jessie
Add . /code
WORKDIR /code
RUN pip install -r requirements.txt
WORKDIR /code/src/endpoints
CMD ["python3", "main.py"]