# Cache project

## Description

Application is supposed to be used as caching proxy for external API.

## Installation & Run

### Prerequisites

In order to run application on your local machine you need to install following tools

* Python 3.9
* Git client
* Docker & Docker compose

### Configuration

Create `api.env` file in the env folder and fill it with appropriate values

```shell
API_URL=https://example.com
ACCESS_TOKEN=1a2b3c4d5e
```

### Run

Use `docker-compose` command to launch application

```shell
docker-compose up
```

Now you can access browsable API at `http://localhost:8000` and UI at `http://localhost`

## Development

### Prerequisites

After fulfilling Installation & Run prerequisites you need to create a virtual environment in the project folder and
install project dependencies

```shell
cd cache
python3.9 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

### Test

To run tests open terminal, cd into project folder, activate virtual environment and issue `pytest` command

```shell
cd cache
. venv/bin/activate
pytest
```
