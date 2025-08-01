# mini-rag

This is a minimal implementation of the RAG model for question answering.

## Requirements

- Python 3.9 or later

#### Install Python using MiniConda

1) Download and install MiniConda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)
2) Create a new environment using the following command:
```bash
$ conda create -n mini-rag python=3.9
```
3) Activate the environment:
```bash
$ conda activate mini-rag
```

## Installation

### Install the required packages

```bash
$ cd src
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file. Like `GEMINI_API_KEY` value.

## Run FastAPI server

```bash
$ uvicorn main:app --reload --host 127.0.0.1 --port 8000
```