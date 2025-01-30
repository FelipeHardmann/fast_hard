import click
from pathlib import Path
from fast_hard.utils.project_initializer import initialize_project_structure

STRUCTURE_CHOICES = ["mvc", "use_cases"]

DATABASE_CHOICES = ["sqlite", "mysql", "postgresql", "mongodb"]


@click.group()
def cli():
    pass


@cli.command(name="create_project")
@click.argument("project_name")
@click.option(
    "--structure",
    type=click.Choice(STRUCTURE_CHOICES),
    required=True,
    help="Escolha a estrutura de pastas (MVC ou Use Cases)"
)
@click.option(
    "--database",
    type=click.Choice(DATABASE_CHOICES),
    required=True,
    help="Escolha o banco de dados"
)
def create_project(project_name, structure, database):
    initialize_project_structure(project_name, database)

    if structure == "mvc":
        create_mvc_structure(project_name)
    elif structure == "use_cases":
        create_use_cases_structure(project_name)

    click.echo(f"Projeto {project_name} criado com sucesso com a estrutura {structure} e banco de dados {database}!")


def create_mvc_structure(project_name):
    project_path = Path(project_name)
    app_path = project_path / "app"

    # Cria pastas do MVC
    (app_path / "controllers").mkdir(exist_ok=True)
    (app_path / "views").mkdir(exist_ok=True)
    (app_path / "models").mkdir(exist_ok=True)

    # Cria arquivos de exemplo
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


def create_use_cases_structure(project_name):
    project_path = Path(project_name)
    app_path = project_path / "app"

    use_cases_path = app_path / "use_cases"
    use_cases_path.mkdir(exist_ok=True)
    (use_cases_path / "__init__.py").write_text("")

    (use_cases_path / "example_use_case.py").write_text("""class ExampleUseCase:
    def execute(self):
        # Lógica do caso de uso
        return {"message": "Caso de uso executado com sucesso!"}
""")

    click.echo(f"Estrutura de casos de uso criada em {use_cases_path}.")


if __name__ == "__main__":
    cli()
