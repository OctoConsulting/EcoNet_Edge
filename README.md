
# EchoNet Edge

Official Repo for EchoNet Edge.
## Contents

| Functionality |     Desciption                                                      |
| ----------------- | ------------------------------------------------------------------ |
| [Main Program](#Main) |  |
| [API](#API) |  |
| [Drone Protocal](#Drone-Protocol) |  |
| [Drone Managment](#Drone-Management) |  |
| [Shot Detection](#Shot-Detection) |  |
| [Preprossessing](#Preprossessing) |  |



## Installation

Install my-project with npm

```bash
  npm install my-project
  cd my-project
```
    
## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```


## Main

## API
This is a centralized API that manages communication with other EchoNet microservices.
## API Reference

#### Get list of detection endpoints 

```http
  GET /api/detections
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get list of drone endpoints 

```http
  GET /api/drone/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### Get list of toto endpoints 

```http
  GET /api/toto/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### Get list of surge endpoints 

```http
  GET /api/surge/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |


## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd Edge_API
```

```making a vitual enviroment

  python -m venv .venv

  .venv/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  flask run
```

## Drone Protocol
Setting up a dev environment:

Prereq: Docker

Navigate to Edge_Parrot/dev_env_setup

run:
```Bash
chmod +x setup.sh
./setup.sh
```
if you need Sphinx, run ./postinst.sh inside the container

## Drone Management 
## Shot Detection
## Preprossessing
