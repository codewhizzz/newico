import os
from sqlalchemy import engine_from_config, pool
from alembic import context
from sqlmodel import SQLModel
# Ensure all your model imports are correctly handled
from app.models import Bookmark, Document, Entity

# Load the database URL from an environment variable
sqlalchemy_url = os.getenv('DATABASE_URL')
if not sqlalchemy_url:
    raise Exception("DATABASE_URL environment variable not set")

config = context.config
# Set the SQLAlchemy URL for Alembic
config.set_main_option("sqlalchemy.url", sqlalchemy_url)

# Alembic configuration for logging
if config.config_file_name is not None:
    from logging.config import fileConfig
    fileConfig(config.config_file_name)

target_metadata = SQLModel.metadata

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
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
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
        url=sqlalchemy_url  # Directly use sqlalchemy_url
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

