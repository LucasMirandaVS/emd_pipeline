from etl.extract import get_csv_links

def test_get_csv_links():
    links = get_csv_links()
    assert isinstance(links, list)
    assert all(link.endswith(".csv") for link in links)
    assert any("terceirizados" in link for link in links)
