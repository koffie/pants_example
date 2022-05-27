# My Subproject

My Subproject is a [Zero MQ](https://zeromq.org/) based application, either functioning as a server or a client.

## Installation


```bash
poetry install
```

## Usage

```bash
poetry run serve
```

or

```bash
poetry shell
serve
```

## Testing

```bash
pytest .
```

## Linting

```bash
mypy .
black --check .
isort --check .
pylint my_subproject
```
