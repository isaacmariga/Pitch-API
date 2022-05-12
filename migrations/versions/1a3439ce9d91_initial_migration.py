"""Initial Migration

Revision ID: 1a3439ce9d91
Revises: c87e760a3269
Create Date: 2022-05-12 09:14:31.652391

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a3439ce9d91'
down_revision = 'c87e760a3269'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.Column('vote_number', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('upvotes')
    op.drop_table('downvotes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('downvotes',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], name='downvotes_pitch_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='downvotes_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='downvotes_pkey')
    )
    op.create_table('upvotes',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], name='upvotes_pitch_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='upvotes_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='upvotes_pkey')
    )
    op.drop_table('votes')
    # ### end Alembic commands ###
