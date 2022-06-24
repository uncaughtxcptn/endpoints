# endpoints

View and send custom responses to requests on HTTP endpoints.

![endpoints](screenshot.png)


## Running this project

This project requires **Python >=3.5**, **NodeJS >=6.0**, redis and postgresql. Please make sure to have them installed on your system.

Follow the following steps in order to setup and run this project:

```bash
# Clone the repository
$ git clone https://github.com/uncaughtxcptn/endpoints.git
$ cd endpoints

# Install dependencies
$ pip install -r requirements.txt
$ npm install

# Build frontend assets
$ npm run build
$ npm run build:watch  # You can also auto-compile assets as they change

# For production build of assets, NODE_ENV needs to be specified
$ NODE_ENV=production npm run build

# Make sure to create a postgres database 
$ createdb endpoints
# Make sure that redis is running (you need a separate terminal for this)
$ redis-server
# Run the Web server
$ cd src/endpoints
$ python main.py
```

You can also run the application using docker. Make sure docker and docker-compose is installed in your system

```console
$ docker-compose up
# the app will be running at localhost:8080
```

On Apple Silicon, run the following with platform-specific build

```console
$ docker build --platform=linux/x86_64 .
[+] Building 170.5s (14/14) FINISHED
...
```

## License

MIT License
