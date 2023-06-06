
# EchoNet API

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

