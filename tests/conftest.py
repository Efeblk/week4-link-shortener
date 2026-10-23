import pytest

import main


@pytest.fixture(autouse=True)
def fresh_db(tmp_path, monkeypatch):
    """Give every test its own empty database, so tests are independent and never
    touch the real links.db used by the running app."""
    monkeypatch.setattr(main, "DB_PATH", tmp_path / "links.db")
    main.init_db()
    yield
