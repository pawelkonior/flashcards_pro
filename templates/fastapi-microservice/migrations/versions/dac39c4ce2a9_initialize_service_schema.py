"""initialize service schema

Revision ID: dac39c4ce2a9
Revises:
Create Date: 2026-09-17 21:55:56.513588

"""

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "dac39c4ce2a9"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""


def downgrade() -> None:
    """Downgrade schema."""
