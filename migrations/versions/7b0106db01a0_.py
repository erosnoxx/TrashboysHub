"""empty message

Revision ID: 7b0106db01a0
Revises: 
Create Date: 2023-11-17 12:53:51.111817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b0106db01a0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(length=50), nullable=False),
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('salt', sa.String(length=255), nullable=False),
    sa.Column('gender', sa.String(), nullable=False),
    sa.Column('birth', sa.Date(), nullable=False),
    sa.Column('reg_date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('published', sa.Boolean(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.Column('text', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    op.drop_table('user')
    op.drop_table('category')
    # ### end Alembic commands ###