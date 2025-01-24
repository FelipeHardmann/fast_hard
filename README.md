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

## Installation

You can install `fast_hard` via pip:

```bash
pip install fast_hard

fast-hard my_new_project

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

# Running the Project

cd my_new_project

pip install -r requirements.txt

cd app
uvicorn main:app --reload

http://127.0.0.1:8000/

You should see the message:

{
  "Hello": "World"
}

# Link PyPi
https://pypi.org/project/fast-hard/
