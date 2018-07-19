"""initial db

Revision ID: 832ae5f99513
Revises: 
Create Date: 2018-07-19 21:10:21.855850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '832ae5f99513'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('published_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###
