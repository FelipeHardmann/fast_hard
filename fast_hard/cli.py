import click
from pathlib import Path


def initialize_project_structure(project_name):
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


@click.group()
def cli():
    pass


@cli.command(name="create_project")
@click.argument("project_name")
def create_project(project_name):
    initialize_project_structure(project_name)


@cli.command(name="create_use_cases")
@click.argument("project_name")
def create_use_cases(project_name):
    project_path = Path(project_name)
    app_path = project_path / "app"

    if not app_path.exists():
        click.echo(f"O projeto {project_name} não existe. Criando projeto...")
        initialize_project_structure(project_name)

    use_cases_path = app_path / "use_cases"
    use_cases_path.mkdir(exist_ok=True)
    (use_cases_path / "__init__.py").write_text("")

    (use_cases_path / "example_use_case.py").write_text("""class ExampleUseCase:
    def execute(self):
        # Lógica do caso de uso
        return {"message": "Caso de uso executado com sucesso!"}
""")

    click.echo(f"Estrutura de casos de uso criada em {use_cases_path}.")


@cli.command(name="create_mvc")
@click.argument("project_name")
def create_mvc(project_name):
    project_path = Path(project_name)
    app_path = project_path / "app"

    if not app_path.exists():
        click.echo(f"O projeto {project_name} não existe. Criando projeto...")
        initialize_project_structure(project_name)

    (app_path / "controllers").mkdir(exist_ok=True)
    (app_path / "views").mkdir(exist_ok=True)
    (app_path / "models").mkdir(exist_ok=True)

    (app_path / "controllers" / "__init__.py").write_text("")
    (app_path / "controllers" / "example_controller.py").write_text("""from fastapi import APIRouter

router = APIRouter()

@router.get("/example")
def example():
    return {"message": "Exemplo de controller"}
""")

    (app_path / "views" / "__init__.py").write_text("")
    (app_path / "views" / "example_view.py").write_text("""# Exemplo de view (se necessário)
""")

    (app_path / "models" / "__init__.py").write_text("")
    (app_path / "models" / "example_model.py").write_text("""from sqlalchemy import Column, Integer, String
from app.config.database import Base

class ExampleModel(Base):
    __tablename__ = "examples"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
""")

    click.echo(f"Estrutura MVC criada em {app_path}.")


if __name__ == "__main__":
    cli()
