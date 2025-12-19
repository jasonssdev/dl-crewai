# dl-crewai

[![Python](https://img.shields.io/badge/python-3.12%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![CrewAI](https://img.shields.io/badge/CrewAI-agents-black)](https://www.crewai.com/)
[![uv](https://img.shields.io/badge/uv-package%20manager-purple)](https://github.com/astral-sh/uv)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A minimal **CrewAI** project for experimenting with agent-based workflows in Python.

## Quickstart

### Prerequisites

- Python 3.12+
- `uv` (recommended)

### Install

Install `uv`:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Create the lockfile (using your current Python):

```sh
uv lock --python "$(which python)"
```

Install dependencies:

```sh
uv pip install 'crewai[tools]'
```

### Run

```sh
python main.py
```
