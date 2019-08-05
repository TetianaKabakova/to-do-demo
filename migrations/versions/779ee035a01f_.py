"""empty message

Revision ID: 779ee035a01f
Revises: 
Create Date: 2019-08-05 11:08:36.559964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '779ee035a01f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_todo_list_timestamp'), 'todo_list', ['timestamp'], unique=False)
    op.create_index(op.f('ix_todo_list_title'), 'todo_list', ['title'], unique=True)
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=256), nullable=True),
    sa.Column('todo_list_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['todo_list_id'], ['todo_list.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    op.drop_index(op.f('ix_todo_list_title'), table_name='todo_list')
    op.drop_index(op.f('ix_todo_list_timestamp'), table_name='todo_list')
    op.drop_table('todo_list')
    # ### end Alembic commands ###
