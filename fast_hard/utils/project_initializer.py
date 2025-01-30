from pathlib import Path
from fast_hard.templates import sqlite, mysql, postgresql, mongodb


DATABASE_TEMPLATES = {
    "sqlite": {
        "env": sqlite.SQLITE_ENV_TEMPLATE,
        "alembic": sqlite.SQLITE_ALEMBIC_TEMPLATE
    },
    "mysql": {
        "env": mysql.MYSQL_ENV_TEMPLATE,
        "alembic": mysql.MYSQL_ALEMBIC_TEMPLATE
    },
    "postgresql": {
        "env": postgresql.POSTGRESQL_ENV_TEMPLATE,
        "alembic": postgresql.POSTGRESQL_ALEMBIC_TEMPLATE
    },
    "mongodb": {
        "env": mongodb.MONGODB_ENV_TEMPLATE,
        "alembic": mongodb.MONGODB_ALEMBIC_TEMPLATE
    }
}


def initialize_project_structure(project_name, database):
    project_path = Path(project_name)
    project_path.mkdir(parents=True, exist_ok=True)

    app_path = project_path / "app"
    app_path.mkdir(exist_ok=True)
    (app_path / "models").mkdir(exist_ok=True)
    (app_path / "schemas").mkdir(exist_ok=True)
    (app_path / "routes").mkdir(exist_ok=True)
    (app_path / "tests").mkdir(exist_ok=True)
    (app_path / "config").mkdir(exist_ok=True)
    (app_path / "alembic").mkdir(exist_ok=True)
    (app_path / "alembic" / "versions").mkdir(exist_ok=True)

    (app_path / "__init__.py").write_text("")
    (app_path / "main.py").write_text("""from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
""")

    (project_path / ".env").write_text(DATABASE_TEMPLATES[database]["env"])

    (project_path / "alembic.ini").write_text(
        DATABASE_TEMPLATES[database]["alembic"]
    )

    (project_path / "requirements.txt").write_text("""fastapi
uvicorn
sqlalchemy
pytest
email-validator
alembic
""")

    (project_path / ".gitignore").write_text("""# Ignorar arquivos
__pycache__/
*.pyc
*.pyo
*.pyd
*.db
*.sqlite3
.env
""")

    (project_path / "README.md").write_text(f"""# {project_name}

Este é um projeto FastAPI gerado automaticamente.
""")
