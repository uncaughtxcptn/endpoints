# endpoints

View and send custom responses to requests on HTTP endpoints.

![endpoints](screenshot.png)


## Running this project

This project requires **Python >=3.5** and **NodeJS >=6.0**. Please make sure to have them installed on your system.

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

# TODO: Add how to run the Python project
```


## License

MIT License
