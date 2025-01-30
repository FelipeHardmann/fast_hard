# Fast Hard

Fast Hard is a Python package that generates a FastAPI project with a basic structure, similar to `create-react-app` for React. It sets up a ready-to-use FastAPI application with essential dependencies, folder structure, and configurations.

---

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
- **New commands for flexible folder structure**:
  - `fast-hard create_mvc <project_name>`: Creates a project and adds an MVC folder structure.
  - `fast-hard create_use_cases <project_name>`: Creates a project and adds a folder structure for use cases.
- **Choose your database**:
  - SQLite
  - MySQL
  - PostgreSQL
  - MongoDB

---

## Installation

You can install `fast_hard` via pip:

```bash
pip install fast_hard
```

---

## Usage

### Create a New Project

To create a new project, use the following command:

```bash
fast-hard create_project <project_name> --structure <structure> --database <database>
```

- `<project_name>`: The name of your new project.
- `--structure`: Choose the folder structure (`mvc` or `use_cases`).
- `--database`: Choose the database (`sqlite`, `mysql`, `postgresql`, or `mongodb`).

**Example:**

```bash
fast-hard create_project my_new_project --structure mvc --database mysql
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

---

### Add an MVC Structure

To add an MVC structure to an existing project (or create a new one if it doesn't exist), use:

```bash
fast-hard create_mvc <project_name>
```

This will add the following folders under the `app` directory:

```
my_new_project/
├── app/
│   ├── controllers/
│   ├── views/
│   └── models/
```

---

### Add a Use Case Structure

To add a use case structure to an existing project (or create a new one if it doesn't exist), use:

```bash
fast-hard create_use_cases <project_name>
```

This will add the following folder under the `app` directory:

```
my_new_project/
├── app/
│   ├── use_cases/
```

---

### Run the Project

To run the project, navigate to the project directory and start the FastAPI server:

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

---

## Database Configuration

The `.env` file will be configured based on the chosen database:

### SQLite
```plaintext
DATABASE_URL=sqlite:///./test.db
```

### MySQL
```plaintext
DATABASE_URL=mysql+pymysql://user:password@localhost/dbname
```

### PostgreSQL
```plaintext
DATABASE_URL=postgresql://user:password@localhost/dbname
```

### MongoDB
```plaintext
DATABASE_URL=mongodb://localhost:27017/
```

Make sure to update the `.env` file with your actual database credentials.

---

## Link PyPI

[Fast Hard on PyPI](https://pypi.org/project/fast-hard/)

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

