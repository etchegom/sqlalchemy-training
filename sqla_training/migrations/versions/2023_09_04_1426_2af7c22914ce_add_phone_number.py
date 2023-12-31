"""add phone number

Revision ID: 2af7c22914ce
Revises: 2aa3a3ca9b8b
Create Date: 2023-09-04 14:26:30.014052

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "2af7c22914ce"
down_revision: Union[str, None] = "2aa3a3ca9b8b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("user", sa.Column("phone_number", sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "phone_number")
    # ### end Alembic commands ###
