MYSQL_ENV_TEMPLATE = """# Variáveis de ambiente
DATABASE_URL=mysql+pymysql://user:password@localhost/dbname
"""

MYSQL_ALEMBIC_TEMPLATE = """[alembic]
script_location = app/alembic
sqlalchemy.url = mysql+pymysql://user:password@localhost/dbname
"""
