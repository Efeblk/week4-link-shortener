from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_shorten_and_redirect():
    r = client.post("/shorten", json={"url": "https://example.com"})
    assert r.status_code == 200
    code = r.json()["code"]
    assert code
    r2 = client.get(f"/{code}", follow_redirects=False)
    assert r2.status_code == 307
    assert r2.headers["location"] == "https://example.com"


def test_rejects_bad_url():
    r = client.post("/shorten", json={"url": "ftp://nope"})
    assert r.status_code == 400


def test_unknown_code_404():
    r = client.get("/does-not-exist", follow_redirects=False)
    assert r.status_code == 404


def test_new_link_stats_start_at_zero_and_reads_do_not_count_clicks():
    created = client.post("/shorten", json={"url": "https://example.com"})
    code = created.json()["code"]

    first_stats = client.get(f"/stats/{code}")
    second_stats = client.get(f"/stats/{code}")

    assert first_stats.status_code == 200
    assert first_stats.json() == {"url": "https://example.com", "clicks": 0}
    assert second_stats.json()["clicks"] == 0


def test_visiting_a_link_increments_its_click_count():
    created = client.post("/shorten", json={"url": "https://example.com"})
    code = created.json()["code"]

    first_visit = client.get(f"/{code}", follow_redirects=False)
    second_visit = client.get(f"/{code}", follow_redirects=False)
    stats = client.get(f"/stats/{code}")

    assert first_visit.status_code == 307
    assert second_visit.status_code == 307
    assert stats.json()["clicks"] == 2


def test_stats_for_an_unknown_code_returns_404():
    response = client.get("/stats/does-not-exist")

    assert response.status_code == 404


def test_links_track_clicks_independently():
    first = client.post("/shorten", json={"url": "https://first.example"}).json()
    second = client.post("/shorten", json={"url": "https://second.example"}).json()

    client.get(f"/{first['code']}", follow_redirects=False)
    client.get(f"/{first['code']}", follow_redirects=False)
    client.get(f"/{second['code']}", follow_redirects=False)

    first_stats = client.get(f"/stats/{first['code']}")
    second_stats = client.get(f"/stats/{second['code']}")

    assert first_stats.json()["clicks"] == 2
    assert second_stats.json()["clicks"] == 1
