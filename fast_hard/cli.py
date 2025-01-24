# fast_hard/cli.py
import click
from pathlib import Path


@click.command()
@click.argument('project_name')
def create_project(project_name):
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

    (project_path / "requirements.txt").write_text("""fastapi
uvicorn
sqlalchemy
pytest
email-validator
alembic
""")

    (project_path / ".env").write_text("""# Variáveis de ambiente
DATABASE_URL=sqlite:///./test.db
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

    (project_path / "alembic.ini").write_text(f"""[alembic]
script_location = app/alembic
sqlalchemy.url = sqlite:///./test.db

[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARN
handlers = console
qualname =

[logger_sqlalchemy]
level = WARN
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S
""")

    (project_path / "README.md").write_text(f"""# {project_name}

Este é um projeto FastAPI gerado automaticamente.
""")

    click.echo(f"Projeto {project_name} criado com sucesso!")

if __name__ == "__main__":
    create_project()