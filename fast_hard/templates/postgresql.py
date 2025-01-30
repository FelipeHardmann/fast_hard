POSTGRESQL_ENV_TEMPLATE = """# Variáveis de ambiente
DATABASE_URL=postgresql://user:password@localhost/dbname
"""

POSTGRESQL_ALEMBIC_TEMPLATE = """[alembic]
script_location = app/alembic
sqlalchemy.url = postgresql://user:password@localhost/dbname
"""
