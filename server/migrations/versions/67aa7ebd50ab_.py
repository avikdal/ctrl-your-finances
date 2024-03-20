"""empty message

Revision ID: 67aa7ebd50ab
Revises: 
Create Date: 2024-03-20 16:27:27.749349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67aa7ebd50ab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('households',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plaid_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('access_token', sa.Text(), nullable=True),
    sa.Column('item_id', sa.Text(), nullable=True),
    sa.Column('cursor', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Text(), nullable=True),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('institution_name', sa.Text(), nullable=True),
    sa.Column('household_id', sa.Integer(), nullable=True),
    sa.Column('plaid_item_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['household_id'], ['households.id'], name=op.f('fk_accounts_household_id_households')),
    sa.ForeignKeyConstraint(['plaid_item_id'], ['plaid_items.id'], name=op.f('fk_accounts_plaid_item_id_plaid_items')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('email', sa.Text(), nullable=False),
    sa.Column('household_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['household_id'], ['households.id'], name=op.f('fk_users_household_id_households')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('account_users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['accounts.id'], name=op.f('fk_account_users_account_id_accounts')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_account_users_user_id_users')),
    sa.PrimaryKeyConstraint('user_id', 'account_id')
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('authorized_date', sa.Text(), nullable=True),
    sa.Column('merchant_name', sa.Text(), nullable=True),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('personal_finance_category', sa.Text(), nullable=True),
    sa.Column('transaction_id', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['users.id'], name=op.f('fk_transactions_account_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    op.drop_table('account_users')
    op.drop_table('users')
    op.drop_table('accounts')
    op.drop_table('plaid_items')
    op.drop_table('households')
    # ### end Alembic commands ###
