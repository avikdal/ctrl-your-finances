"""empty message

Revision ID: dc33aebcca93
Revises: 
Create Date: 2024-03-18 10:06:16.048884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc33aebcca93'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plaid_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('access_token', sa.Text(), nullable=True),
    sa.Column('item_id', sa.Text(), nullable=True),
    sa.Column('cursor', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('email', sa.Text(), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('plaid_item_id', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('authorized_date', sa.Text(), nullable=True),
    sa.Column('merchant_name', sa.Text(), nullable=True),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('personal_finance_category', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['plaid_item_id'], ['plaid_items.id'], name=op.f('fk_transactions_plaid_item_id_plaid_items')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_transactions_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    op.drop_table('users')
    op.drop_table('plaid_items')
    # ### end Alembic commands ###
