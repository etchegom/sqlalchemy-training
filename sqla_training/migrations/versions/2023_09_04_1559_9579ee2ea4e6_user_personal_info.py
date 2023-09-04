"""user personal info

Revision ID: 9579ee2ea4e6
Revises: 2af7c22914ce
Create Date: 2023-09-04 15:59:54.905027

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy_utils import StringEncryptedType

# revision identifiers, used by Alembic.
revision: str = "9579ee2ea4e6"
down_revision: Union[str, None] = "2af7c22914ce"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("user", sa.Column("personal_info", StringEncryptedType(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "personal_info")
    # ### end Alembic commands ###
