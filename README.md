# IoT Data  

A project with switchbot meter and Raspberry Pi...

## Overview
This example uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Requirements
Python 3.9.x+

## Project

### Run the project
To start the whole stack, you can run it using docker-compose:
```bash
docker-compose up -d
```

### [IoT data api](iot_data_api)

A server using Flask that exposes api to save temperature and humidity data.

#### Usage
To run the server, please execute the following from the [iot_data_api](iot_data_api) directory:

```
cd iot_data_api
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m app
```

and open your browser to [http://localhost:8080/openapi.yaml](http://localhost:8080/openapi.yaml)

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

#### Running with Docker

To run the server on a Docker container, please execute the following from the [iot_data_api](iot_data_api) directory:

```bash
# building the image
docker build -t iot_data_api .

# starting up a container
docker run -p 8080:8080 iot_data_api
```