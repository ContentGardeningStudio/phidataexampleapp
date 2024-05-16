# phidataexampleapp

This is an example AI app with assistants based on phidata. This AI app is built with Streamlit, PgVector, and local LLMs using ollama. You can run it locally using Docker.

## 1. [Install](https://hub.docker.com/r/ollama/ollama) ollama wit docker and run models

### Run Ollama locally on docker

Set up the same network as the app network `ai` by default:

```shell
docker run -d -v ollama:/root/.ollama --name ollama --network ai ollama/ollama
```

### Run chat and embedding models

```shell
# run llama3
docker exec -it ollama ollama run llama3

# run nomic-embed-text
docker exec -it ollama ollama run nomic-embed-text
```

Message `/bye` to exit the chat model

## 2. Create a virtual environment

Open the Terminal and create a python virtual environment.

```shell
python3 -m venv venv
source ./venv/bin/activate
```

## 3. Install phidata

Install phidata using pip

```shell
pip install -U "phidata[aws]"
```

## 4. Set environment variables

Add the following line to your `.env` file to allow the app to connect with Ollama in the same Docker network `ai` by default:

```shell
OLLAMA_HOST="http://ollama:11434"
```

## 5. Build your development image

Build the development image using:

```shell
phi ws up --env dev --infra docker --type image
```

To force rebuild images, use the --force or -f flag

```shell
phi ws up --env dev --infra docker --type image --force
```

## 6. Restart all containers

Restart all docker containers using:

```shell
phi ws restart --env dev --infra docker --type container
```

Open localhost:8501 to view your AI Apps.
