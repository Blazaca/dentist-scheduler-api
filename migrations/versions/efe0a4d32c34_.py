"""empty message

Revision ID: efe0a4d32c34
Revises: 
Create Date: 2022-01-25 14:55:55.686531

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efe0a4d32c34'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('preset',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('AllDay', sa.String(length=5), nullable=True),
    sa.Column('Categorize', sa.String(length=5), nullable=True),
    sa.Column('CustomStyle', sa.String(length=15), nullable=True),
    sa.Column('Description', sa.String(length=15), nullable=True),
    sa.Column('EndTime', sa.String(length=25), nullable=True),
    sa.Column('Location', sa.String(length=25), nullable=True),
    sa.Column('Owner', sa.Numeric(precision=2), nullable=True),
    sa.Column('Priority', sa.String(length=15), nullable=True),
    sa.Column('Recurrence', sa.Numeric(precision=3), nullable=True),
    sa.Column('RecurrenceEndDate', sa.String(length=50), nullable=True),
    sa.Column('RecurrenceRule', sa.String(length=50), nullable=True),
    sa.Column('RecurrenceStartDate', sa.String(length=50), nullable=True),
    sa.Column('RecurrenceType', sa.String(length=15), nullable=True),
    sa.Column('RecurrenceTypeCount', sa.String(length=15), nullable=True),
    sa.Column('Reminder', sa.String(length=15), nullable=True),
    sa.Column('StartTime', sa.String(length=50), nullable=True),
    sa.Column('StartTimeZone', sa.String(length=15), nullable=True),
    sa.Column('Subject', sa.String(length=75), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('preset')
    # ### end Alembic commands ###