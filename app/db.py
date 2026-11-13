import json
from contextlib import contextmanager
import psycopg
from psycopg.rows import dict_row
from app.config import get_settings

@contextmanager
def db_connection():
    url = get_settings().database_url
    if not url:
        raise ValueError("Database URL is not set in the environment variables.")
    with psycopg.connect(url, row_factory=dict_row, timeout=10) as conn:
        yield conn

def audit(conn, actor, tenant, action, details):
    """Insert an audit log entry into the database."""
    conn.execute(
        "INSERT INTO audit_events (actor, tenant, action, details) VALUES (%s, %s, %s, %s)",
        (actor, tenant, action, json.dumps(details)),
    )

