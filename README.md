# Fast Hard

Fast Hard is a Python package that generates a FastAPI project with a basic structure, similar to `create-react-app` for React. It sets up a ready-to-use FastAPI application with essential dependencies, folder structure, and configurations.

## Features

- Generates a FastAPI project with a standard folder structure.
- Installs essential dependencies:
  - FastAPI
  - Uvicorn
  - SQLAlchemy
  - Pytest
  - Email-validator
  - Alembic (for database migrations)
- Includes a basic `.env` file for environment variables.
- Sets up Alembic for database migrations.
- Provides a simple `main.py` with a "Hello World" endpoint.
- New commands for flexible folder structure:
  - `fast-hard create_mvc <project_name>`: Creates a project and adds an MVC folder structure.
  - `fast-hard create_use_cases <project_name>`: Creates a project and adds a folder structure for use cases.

## Installation

You can install `fast_hard` via pip:

```bash
pip install fast_hard
```

## Usage

### Create a New Project

```bash
fast-hard create_project my_new_project
```

This will generate a new FastAPI project with the following structure:

```
my_new_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   ├── schemas/
│   ├── routes/
│   ├── tests/
│   ├── config/
│   └── alembic/
│       ├── env.py
│       ├── script.py.mako
│       └── versions/
├── requirements.txt
├── .env
├── .gitignore
├── alembic.ini
└── README.md
```

### Add an MVC Structure

```bash
fast-hard create_mvc my_new_project
```

If the project does not exist, it will first create the project and then add the following folders under the `app` directory:

```
my_new_project/
├── app/
│   ├── controllers/
│   ├── views/
│   └── models/
```

### Add a Use Case Structure

```bash
fast-hard create_use_cases my_new_project
```

If the project does not exist, it will first create the project and then add the following folder under the `app` directory:

```
my_new_project/
├── app/
│   ├── use_cases/
```

### Run the Project

```bash
cd my_new_project
pip install -r requirements.txt
cd app
uvicorn main:app --reload
```

Open your browser at:

```
http://127.0.0.1:8000/
```

You should see the message:

```json
{
  "Hello": "World"
}
```

## Link PyPI

[Fast Hard on PyPI](https://pypi.org/project/fast-hard/)

