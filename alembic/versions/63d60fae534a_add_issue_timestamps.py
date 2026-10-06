"""add issue timestamps

Revision ID: 63d60fae534a
Revises: 
Create Date: 2026-10-07 02:22:13.962229

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '63d60fae534a'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        "issues",
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            server_default=sa.func.now()
        )
    )

    op.add_column(
        "issues",
        sa.Column(
            "updated_at",
            sa.DateTime(),
            nullable=False,
            server_default=sa.func.now()
        )
    )
    
def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column("issues", "updated_at")
    op.drop_column("issues", "created_at")