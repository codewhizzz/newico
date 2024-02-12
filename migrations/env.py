import os
from dotenv import load_dotenv
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from sqlmodel import SQLModel
from alembic import context
from app.models import Bookmark, Document, Entity

# Load environment variables from .env file
load_dotenv()

# Retrieve the database URL from environment variable
connection_string = os.getenv('DATABASE_URL')

# Ensure the connection string is correctly retrieved; otherwise, use a default or log an error
if connection_string is None:
    raise ValueError("DATABASE_URL environment variable not set")

config = context.config
config.set_main_option("sqlalchemy.url", connection_string)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = SQLModel.metadata

def run_migrations_offline() -> None:
    url = connection_string
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
        url=connection_string,  # Ensure the engine uses the provided connection string
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

