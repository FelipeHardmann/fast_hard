MONGODB_ENV_TEMPLATE = """# Variáveis de ambiente
DATABASE_URL=mongodb://localhost:27017/
"""

MONGODB_ALEMBIC_TEMPLATE = """[alembic]
script_location = app/alembic
sqlalchemy.url = mongodb://localhost:27017/
"""
