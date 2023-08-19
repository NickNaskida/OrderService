"""add product relationship

Revision ID: b809d9b50dd7
Revises: c29415aee3cf
Create Date: 2023-08-19 22:38:25.749451

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b809d9b50dd7'
down_revision: Union[str, None] = 'c29415aee3cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'batches', 'products', ['sku'], ['sku'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'batches', type_='foreignkey')
    # ### end Alembic commands ###
