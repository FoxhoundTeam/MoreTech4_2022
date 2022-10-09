"""Added text_prepared and title_prepared

Revision ID: 1c41b5697816
Revises: e07bdc1e64d8
Create Date: 2022-10-09 05:23:40.328923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c41b5697816'
down_revision = 'e07bdc1e64d8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('text_prepared', sa.ARRAY(sa.String()), nullable=False))
    op.add_column('news', sa.Column('title_prepared', sa.ARRAY(sa.String()), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('news', 'title_prepared')
    op.drop_column('news', 'text_prepared')
    # ### end Alembic commands ###