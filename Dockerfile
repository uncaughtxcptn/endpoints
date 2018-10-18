FROM python:3.6-jessie

RUN wget -qO node.tar.xz https://nodejs.org/dist/v8.12.0/node-v8.12.0-linux-x64.tar.xz
RUN tar -xf node.tar.xz
ENV PATH="/node-v8.12.0-linux-x64/bin:${PATH}"

Add . /code
WORKDIR /code

RUN pip install -r requirements.txt
RUN npm install
RUN npm run build

WORKDIR /code/src/endpoints
# CMD ["gunicorn", "main:application", "--bind", "localhost:8080", "--worker-class", "aiohttp.GunicornWebWorker"]
CMD ["python3", "main.py"]
