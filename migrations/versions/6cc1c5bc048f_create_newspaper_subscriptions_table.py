"""create-newspaper-subscriptions-table

Revision ID: 6cc1c5bc048f
Revises: 5bca43d0b45e
Create Date: 2024-02-21 22:45:49.909278

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cc1c5bc048f'
down_revision = '5bca43d0b45e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('newspaper_subscription', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('newspaper_subscription', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###