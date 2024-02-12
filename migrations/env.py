import os
from sqlalchemy import engine_from_config, pool
from alembic import context
from sqlmodel import SQLModel
from app.models import Bookmark, Document, Entity

# Directly setting the sqlalchemy_url with proper escaping for special characters
# NOTE: For a more secure approach, consider using environment variables and .env files
sqlalchemy_url = r"postgresql+psycopg2://newsql:b\"+ILa>*nr|8N\Ty@34.133.14.187:5432/mydatabase"

config = context.config
config.set_main_option("sqlalchemy.url", sqlalchemy_url)

if config.config_file_name is not None:
    from logging.config import fileConfig
    fileConfig(config.config_file_name)

target_metadata = SQLModel.metadata

def run_migrations_offline():
    url = sqlalchemy_url
    context.configure(
        url=url, 
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"}
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        configuration=config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
        url=sqlalchemy_url
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

