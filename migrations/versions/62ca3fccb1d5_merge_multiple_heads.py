"""merge multiple heads

Revision ID: 62ca3fccb1d5
Revises: 448bb7a4c887, 843b21e085be
Create Date: 2024-02-12 17:52:22.546593

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
import pgvector
from pgvector.sqlalchemy import Vector


# revision identifiers, used by Alembic.
revision: str = '62ca3fccb1d5'
down_revision: Union[str, None] = ('448bb7a4c887', '843b21e085be')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
