"""Insert student records

Revision ID: 4359f38a07c2
Revises:
Create Date: 2024-10-04 06:03:20.807608

"""

from typing import Sequence, Union
from alembic import op
from sqlalchemy.sql import table, column, text
from sqlalchemy import String, Integer, Date
import sqlalchemy as sa
from datetime import date

# revision identifiers, used by Alembic.
revision: str = "4359f38a07c2"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Define the table and columns you are inserting into
students = table(
    "students",
    column("first_name", String),
    column("last_name", String),
    column("email", String),
    column("date_of_birth", Date),
)


def upgrade():
    # Create the table if it doesn't exist
    conn = op.get_bind()
    table_exists = conn.execute(text(
        "SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'students')"
    )).scalar()

    if not table_exists:
        op.create_table(
            "students",
            sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
            sa.Column("first_name", sa.String(length=100), nullable=True),
            sa.Column("last_name", sa.String(length=100), nullable=True),
            sa.Column("email", sa.String(length=100), nullable=True),
            sa.Column("date_of_birth", sa.Date(), nullable=True),
            sa.PrimaryKeyConstraint("id"),
            sa.UniqueConstraint("email"),
        )
        print("Created students table.")

    # Check if records already exist in the students table
    existing_records = conn.execute(text("SELECT COUNT(*) FROM students")).scalar()

    if existing_records == 0:
        # Insert records only if there are no existing records
        op.bulk_insert(
            students,
            [
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "email": "john.doe@example.com",
                    "date_of_birth": date(2020, 1, 1),
                },
                {
                    "first_name": "Jane",
                    "last_name": "Smith",
                    "email": "jane.smith@example.com",
                    "date_of_birth": date(2010, 2, 2),
                },
            ],
        )
        print("Inserted student records.")
    else:
        print(f"Skipped inserting records. {existing_records} records already present.")


def downgrade():
    # Drop the table only if it exists
    conn = op.get_bind()
    table_exists = conn.execute(text(
        "SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'students')"
    )).scalar()

    if table_exists:
        op.drop_table("students")
        print("Dropped students table.")
    else:
        print("No students table found to drop.")