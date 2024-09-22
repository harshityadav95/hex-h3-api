# HEX-H3-API


### Settin up Python pyenv Linux
```
# Install Pyenv Dependency
$sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

# Setup pyenv
$curl https://pyenv.run | bash

# For ZSH user
$echo -e 'export PYENV_ROOT="$HOME/.pyenv"\nexport PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
$echo -e 'eval "$(pyenv init --path)"\neval "$(pyenv init -)"' >> ~/.bashrc

# Refreshing the Shell
$exec "$SHELL"

# Check pyenv version
$pyenv --version

# View available python version
$pyenv install --list

# Install python version
$pyenv install 3.12.0

# Setpyenv version
$python global 3.12.0
$python local 3.12.0
$python shell 3.12.0

# Install  pip
$python -m pip install --upgrade pip



```
$ pip install virtualenv
$ python -m venv venv

# Activate virtualenv
```
#Windows
$ env/Scripts/activate

#Linux
$ source  venv/bin/activate

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











