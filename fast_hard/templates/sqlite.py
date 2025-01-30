SQLITE_ENV_TEMPLATE = """# Variáveis de ambiente
DATABASE_URL=sqlite:///./test.db
"""

SQLITE_ALEMBIC_TEMPLATE = """[alembic]
script_location = app/alembic
sqlalchemy.url = sqlite:///./test.db
"""
