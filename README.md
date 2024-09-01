# HEX-H3-API


## Setting up Virtual Environment
```
$ pip install virtualenv
$ python -m venv env

# Activate virtualenv windows
$ env/Scripts/activate
# Activate virtualenv in linux
$source .venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

```

## Run test case 
To run all the test cases 
```
pytest 
```

## Setup FastAPI
```
pip install "fastapi[standard]"
```

## Run Fastapi Server
```
# Development mode
$ fastapi dev main.py

# Production mode
$ fastapi run main.py
```

## Build docker image
```
$ docker build -t fastapistarter .

$ docker run -d --name mycontainer -p 80:80 fastapistarter

$ docker stop mycontainer
``

## Reference
- https://fastapi.tiangolo.com/fastapi-cli/











