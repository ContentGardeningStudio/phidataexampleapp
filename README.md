# phidataexampleapp

This is an example AI app with assistants based on phidata. This AI app is built with Streamlit, PgVector, and local LLMs using ollama. You can run it locally using Docker.

## Setup Workspace

1. Clone the git repo

> from the `ai-app` dir:

2. Create + activate a virtual env:

```shell
python3 -m venv venv
source ./venv/bin/activate
```

3. Install dependencies:

```sh
./scripts/install.sh
```

4. Setup workspace:

```sh
phi ws setup
```

5. upgraded `phidata`:

```sh
pip install -U phidata
```

## Run AI App locally

1. Start the workspace using:

```sh
phi ws up
```

2. Pull the llama3 and nomic-embed-text models (run this command only once during the initial workspace setup):

```sh
scripts/pull_ollama_models.sh
```

- Open [localhost:8501](http://localhost:8501) to view the Streamlit App.

3. Stop the workspace using:

```sh
phi ws down
```

## Build your development image

Build the development image using:

```shell
phi ws up --env dev --infra docker --type image
```

To force rebuild images, use the --force or -f flag

```shell
phi ws up --env dev --infra docker --type image --force
```

## Restart all containers

Restart all docker containers using:

```shell
phi ws restart --env dev --infra docker --type container
```
