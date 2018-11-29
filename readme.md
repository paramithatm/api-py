# Simple Python API

> A simple CRUD API made using [flask](http://flask.pocoo.org/) connected to [mongoDB](https://www.mongodb.com/) for learning purposes.

## Getting Started

#### Using Docker

To run the project via docker, do the following:

1. Install [Docker](https://docs.docker.com/)
2. Run docker
3. Pull and run the image
```
docker pull paramithatm/python-api
docker run --name python-api -p 5000:5000 paramithatm/python-api
```
4. If you want to terminate it, run `docker stop paramithatm/python-api`

#### Using Git

To run the project locally, do the following:
1. Clone to your local machine `git clone https://github.com/paramithatm/api-py.git`
2. `cd api-py` to enter the directory
3. Install the requirements using `pip install -r requirements.txt`
4. Run using `python3 app.py`

## ☑ TODO

- [ ] Add .env file containing mongodb url since the IP address allowed to access is limited

## Features

- [X] Get
- [x] Get with one parameter
- [X] Post
- [ ] Post image, files
- [ ] Put
- [ ] Delete