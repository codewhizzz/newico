"""Camel case Concept

Revision ID: 0ef4645ca76f
Revises: 70637a1027f0
Create Date: 2024-01-05 09:15:51.015110

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
import pgvector
from pgvector.sqlalchemy import Vector


# revision identifiers, used by Alembic.
revision: str = '0ef4645ca76f'
down_revision: Union[str, None] = '70637a1027f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
