from contextlib import closing

import pytest

from main import get_db


@pytest.fixture(autouse=True)
def reset_link_state():
    """Keep HTTP tests independent by clearing the local service state."""
    with closing(get_db()) as conn:
        conn.execute("DELETE FROM links")
        conn.execute("DELETE FROM sqlite_sequence WHERE name = 'links'")
        conn.commit()
    yield
