"""create initial tables

Revision ID: 16168eab777e
Revises:
Create Date: 2023-03-03 08:37:28.568565

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '16168eab777e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column(
            'id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'),
            nullable=False),
        sa.Column('username', sa.String(length=128), nullable=False),
        sa.Column('password', sa.String(length=128), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)

    op.create_table(
        'event_types',
        sa.Column(
            'id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'),
            nullable=False),
        sa.Column('user_id', postgresql.UUID(), nullable=True),
        sa.Column('type', sa.String(length=512), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_event_types_id'), 'event_types', ['id'], unique=False)

    op.create_table(
        'plants',
        sa.Column(
            'id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'),
            nullable=False),
        sa.Column('user_id', postgresql.UUID(), nullable=True),
        sa.Column('type', sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_plants_id'), 'plants', ['id'], unique=False)

    op.create_table(
        'events',
        sa.Column(
            'id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'),
            nullable=False),
        sa.Column('plant_id', postgresql.UUID(), nullable=True),
        sa.Column('event_type_id', postgresql.UUID(), nullable=True),
        sa.Column('date', sa.DateTime(), nullable=True),
        sa.Column('comment', sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(['event_type_id'], ['event_types.id'], ),
        sa.ForeignKeyConstraint(['plant_id'], ['plants.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_events_id'), 'events', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_events_id'), table_name='events')
    op.drop_table('events')
    op.drop_index(op.f('ix_plants_id'), table_name='plants')
    op.drop_table('plants')
    op.drop_index(op.f('ix_event_types_id'), table_name='event_types')
    op.drop_table('event_types')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
