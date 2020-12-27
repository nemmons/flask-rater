"""empty message

Revision ID: 2090c7a5c43d
Revises: 
Create Date: 2020-11-23 14:22:38.120824

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2090c7a5c43d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rating_manuals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rating_step_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rating_steps',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('rating_manual_id', sa.Integer(), nullable=True),
                    sa.Column('rating_step_type_id', sa.Integer(), nullable=True),
                    sa.Column('name', sa.String(length=50), nullable=True),
                    sa.Column('description', sa.String(length=255), nullable=True),
                    sa.Column('step_order', sa.Integer(), nullable=True),
                    sa.Column('target', sa.String(length=50), nullable=True),
                    sa.Column('created', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['rating_manual_id'], ['rating_manuals.id'], ),
                    # sa.ForeignKeyConstraint(['rating_step_type_id'], ['rating_step_types.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('rating_step_parameters',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('rating_manual_id', sa.Integer(), nullable=True),
                    sa.Column('rating_step_id', sa.Integer(), nullable=True),
                    sa.Column('parameter_order', sa.Integer(), nullable=True),
                    sa.Column('label', sa.String(length=50), nullable=True),
                    sa.Column('value', sa.String(length=50), nullable=True),
                    sa.Column('created', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['rating_manual_id'], ['rating_manuals.id'], ),
                    sa.ForeignKeyConstraint(['rating_step_id'], ['rating_steps.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rating_step_parameters')
    op.drop_table('rating_steps')
    op.drop_table('rating_step_types')
    op.drop_table('rating_manuals')
    # ### end Alembic commands ###